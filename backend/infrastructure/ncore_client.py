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
    
    def parse_tvshow_title(self, title):
        # Normalize
        title = re.sub(r"[._-]+", " ", title).strip()

        # cut off season or episode markers
        match = re.search(r"(.*?)\b(S\d{1,2}|E\d{1,2}|\d{4})\b", title, re.IGNORECASE)
        if match:
            title = match.group

        # Remove trailing resolution, codec, etc...
        noise_keywords = [
            "WEB", "WEBRip", "WEB-DL", "HDRip", "BDRip", "DVDRip", "HDTV",
            "x264", "x265", "H\.264", "H\.265", "DDP", "DD", "AAC", "Atmos",
            "Hun", "Eng", "EnG", "Fulcrum", "ARROW", "NF", "AMZN", "DSNP",
            "REPACK", "DRTE", "SKST", "KOGi", "B9R", "MiXGROUP"
        ]
        pattern = r"\b(" + "|".join(noise_keywords) + r")\b"
        title = re.sub(pattern, title, flags=re.IGNORECASE)
        
        return re.sub(r"\s+", " ", title).strip()