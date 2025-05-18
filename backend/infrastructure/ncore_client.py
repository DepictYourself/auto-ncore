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
        # seriesList = self.search_torrents(title, TorrentCategory.SHOW)
        # flatList = [series["title"] for series in seriesList]
        seriesList = [
            "Pandora.2019.S02.WEB.h264-BAE",
            "Bevándorlók Ausztráliában S01",
            "Pandora.2019.S01.MiXED.x264-MiXGROUP",
            "Andor.S02.DSNP.WEBRiP.AAC2.0.x264.HuN.EnG-B9R",
            "Bandidos.S01.2024.NF.WEBRiP.AAC2.0.x264.HuN.SpA-B9R",
            "Alexander.The.Making.of.a.God.S01.480p.NF.WEB-DL.DD+5.1.Atmos.H.264.Hun-ARROW",
            "Star.Wars.Andor.S01.HS.WEBRip.x264.HUN.ENG-FULCRUM",
            "Rocklexikon - Benkó Sándor",
            "Beforeigners.S02.HMAX.WEBRip.x264.HUN.NOR-FULCRUM",
            "Sandor.Matyas.1979.S01.Read.Nfo.ReTaiL.DVDRip.x264.Hun-eStone",
            "Vándorlás a természetben S01",
            "Vándorlás a természetben S01",
            "Beforeigners.S01.WEB-DLRip.x264.HUN-Teko",
            "Andor.S01E00.A.Disney.Day.Special.Look.1080p.WEB.h264-KOGi",
            "Pandora.2019.S02.720p.WEB.H264-MiXGROUP",
            "Bevándorlók Ausztráliában S01 1080p",
            "Bevándorlók Ausztráliában S01 720p",
            "Pandora.2019.S01.720p.AMZN.WEB-DL.DDP5.1.H.264-KiNGS",
            "Időbevándorlók S01 720p",
            "Időbevándorlók S01 1080p",
            "Pandora of the Crimson Shell S01 720p",
            "Pandora Hearts S01 720p",
            "Star.Wars.Andor.S02.2160p.APPS.WEB-DL.DDP.Atmos.5.1.H.265.HuN-GOODWILL",
            "Star.Wars.Andor.S02E01.2160p.APPS.WEB-DL.DDP.Atmos.5.1.H.265.HuN-GOODWILL",
            "Andor.S02.1080p.DSNP.WEB-DL.DDP5.1.Atmos.DV.HDR.H265.HuN.EnG-B9R",
            "Star.Wars.Andor.S02.2160p.DSNP.WEB-DL.P5.Dolby.Vision.DDP5.1.Atmos.h265.HUN-UFO971",
            "Star.Wars.Andor.S02.2160p.DSNP.WEB-DL.DDP5.1.Atmos.DV.HDR.H.265.HUN.ENG-PTHD",
            "Star.Wars.Andor.S02.1080p.DSNP.WEB-DL.DDP5.1.Atmos.H.264.HUN.ENG-PTHD",
            "Star.Wars.Andor.S02.720p.DSNP.WEB-DL.DDP5.1.Atmos.H.264.HUN.ENG-PTHD",
            "Star.Wars.Andor.S01.2160p.DSNP.WEB-DL.P5.Dolby.Vision.DDP-Atmos.5.1.h265.HUN-UFO971",
            "Bandidos.S02.1080p.NF.WEB-DL.DV.HDR.DDP5.1.Atmos.H.265.HUN-FULCRUM",
            "Bandidos.S02.1080p.NF.WEB-DL.DDP5.1.Atmos.H.264.HUN-FULCRUM"
        ]
        # Normalize
        # name = re.sub(r"[._-]+", " ", title).strip()
        testResult = list(map(lambda name: re.sub(r"[._-]+", " ", name).strip(), seriesList))

        return testResult