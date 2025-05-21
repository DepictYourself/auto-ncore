import re
from domain.torrent_category import TorrentCategory
from infrastructure.config_service import ConfigService

from ncoreparser import Client, SearchParamType, Torrent

class NCoreClient:
    def __init__(self, config_service: ConfigService):
        config = config_service.get_ncore_config()
        self.client = Client()
        self.client.login(
            username=config['username'],
            password=config["password"]
        )


    def __enter__(self):
        return self


    def __exit__(self, exc_type, exc_value, traceback):
        if self.client:
            self.client.logout()


    def map_category(self, category: TorrentCategory) -> list[SearchParamType]:
        category_mappings = {
            TorrentCategory.MOVIE: [
                SearchParamType.SD,
                SearchParamType.SD_HUN,
                SearchParamType.HD,
                SearchParamType.HD_HUN
            ],
            TorrentCategory.SHOW: [
                SearchParamType.SDSER,
                SearchParamType.SDSER_HUN,
                SearchParamType.HDSER,
                SearchParamType.HDSER_HUN
            ],
            TorrentCategory.MUSIC: [
                SearchParamType.MP3,
                SearchParamType.MP3_HUN,
                SearchParamType.LOSSLESS,
                SearchParamType.LOSSLESS_HUN,
                SearchParamType.CLIP
            ],
            TorrentCategory.GAME: [
                SearchParamType.GAME_ISO,
                SearchParamType.GAME_RIP,
                SearchParamType.CONSOLE
            ],
            TorrentCategory.SOFTWARE : [
                SearchParamType.ISO,
                SearchParamType.MISC,
                SearchParamType.MOBIL
            ],
            TorrentCategory.EBOOK: [
                SearchParamType.EBOOK,
                SearchParamType.EBOOK_HUN
            ]
        }
        return category_mappings.get(category, [])

    
    def search_torrents(self, pattern: str, category: TorrentCategory, limit: int = 10) -> list[Torrent]:
        ncore_categories = self.map_category(category)

        results = []
        for category in ncore_categories:
            results.extend(self.client.search(
                pattern=pattern,
                type=category,
                number=limit)
            )

        unique_results = {result['id']: result for result in results}.values()
        return list(unique_results)
    

    def list_torrents(self):
        return self.client.get_by_activity()
    

    def get_torrent_info(self, id):
        return self.client.get_torrent(id)
    

    def normalize_tvshow_title(self, title: str) -> str:
        return re.sub(r"[._-]+", " ", title).strip()
    

    def extract_season_episode(self, title: str) -> tuple[str, int |None, int | None]:
        season = episode = None

        # S01E02, S1E2, S01, E01, etc.
        match = re.search(r"S(\d{1,2})(?:E(\d{1,2}))?", title, re.IGNORECASE)
        if match:
            season = int(match.group(1))
            if match.group(2):
                episode = int(match.group(2))
        return title, season, episode
    

     # Remove trailing resolution, codec, etc...
    def remove_technical_info(self, title: str) -> str:
        noise_keywords = [
            "WEB-DL", "WEB-DLRip", "WEB", "WEBRip", "HDRip", "BDRip",
            "x264", "x265", "H.264", "H.265", "DDP","DD\\+2.0", "AAC",
            "Hun-SLN","Hun-eStone", "Hun-BNR","HUN-Teko", "Hun-GOODWILL",
            "Hun", "Eng", "EnG", "NF", "AMZN", "DSNP",  "DRTE", "SKST", "KOGi",
            "SpA-B9R", "B9R", "576p", "720p", "1080p", "1080i", "480p", "480i",
            "Xvid-HSF", "Xvid" "h264-ETHEL", "h264-BAE", "h264", "ETHEL",
            "DDP5.1", "DD5.1", "DD\\+5.1", "AAC2.0", "DAVI", "HDTV",
            "MiXED", "REPACK", "DV", "HDR", "\\.HS", "HMAX", "ARROW",
            "ReTaiL", "NOR-FULCRUM", "Fulcrum", "Read\\.Nfo", "DVDRip", 
            'MiXGROUP', "APPS", "Atmos\\.5\\.1", "Atmos", "2160p", "H265"

        ]
        pattern = r"\b(" + "|".join(noise_keywords) + r")\b"

        result = re.sub(pattern, "", title, flags=re.IGNORECASE)
        return result


    def parse_tvshow_title(self, title):
        name = title
        
        # Remove resolution, codec, encoding, source info
        name = self.remove_technical_info(name)
        # Normalize
        name = self.normalize_tvshow_title(name)

        # Cut off before the season/episode marker
        season_episode_pattern = r"\b(S\d{1,2}(E\d{1,2})?|E\d{1,2}|\d{4})\b"
        name = re.sub(season_episode_pattern, "", name, flags=re.IGNORECASE)

        return re.sub(r"\s+", " ", name).strip()