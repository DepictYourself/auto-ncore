from domain.torrent_category import TorrentCategory
from infrastructure.config_service import ConfigService
from infrastructure.ncore_client import NCoreClient
from infrastructure.transmission_client import TransmissionClient


class TorrentClientService:
    def __init__(self):
        self.config_service = ConfigService()
        self.client = TransmissionClient(self.config_service)

    def list_torrents(self):
        return self.client.get_torrents()
    
    def torrent_info(self, id: int | str):
        return self.client.get_torrent(id)
    
    def add_torrent(self, ncore_torrent_id):
        # TODO: get metadata for download directory
        # metadata = ncore.get_metadata(ncore_torrent_id)

        # TODO: get download directory based on metadata
        # download_dir = KodiDirectoryMapper.get_directory(category=metadata.category)
        download_dir = "/dowloads"
        
        # TODO: Remove the hardcoded torrent url
        ncore_key = self.config_service.get_ncore_config()["key"]
        url = f"https://ncore.pro/torrents.php?action=download&id=3857432&key={ncore_key}"

        return self.client.add_torrent(url, dir=download_dir)
    

    def remove_torrent(self, id: int | str):
        return self.client.remove_torrent(id)
    
    def stop_torrent(self, id: int | str):
        return self.client.stop_torrent(id)
    
    def start_torrent(self, id: int | str):
        return self.client.start_torrent(id)
    

class TrackerService:
    def __init__(self):
        self.client = NCoreClient

    def search_torrent(self, pattern: str, category: TorrentCategory):
        return self.client.search_torrents(pattern, category)