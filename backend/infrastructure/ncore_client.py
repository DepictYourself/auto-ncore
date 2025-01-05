from domain.torrent_category import TorrentCategory
from infrastructure.config_service import ConfigService

from ncoreparser import Client, SearchParamType, ParamSort, ParamSeq

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

    
    def search_torrents(self, pattern: str, category: TorrentCategory, limit: int = 10):
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
    

    def get_torrent_info(self, id):
        return self.client.get_torrent(id)