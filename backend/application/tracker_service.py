from domain.torrent_category import TorrentCategory
from infrastructure.config_service import ConfigService
from infrastructure.ncore_client import NCoreClient


class TrackerService:
    def __init__(self):
        self.config_service = ConfigService()
        self.client = NCoreClient(self.config_service)

    def search_torrent(self, pattern: str, category: TorrentCategory):
        return self.client.search_torrents(pattern, category)
    
    def list_torrents(self):
        return self.client.list_torrents()
    
    def get_details(self, ncore_id):
        return self.client.get_torrent_info(ncore_id)