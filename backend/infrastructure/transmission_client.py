from typing import List
from transmission_rpc import Client, Torrent

from infrastructure.config_service import ConfigService

class TransmissionClient:
    def __init__(self, config_service: ConfigService):
        config = config_service.get_tranmission_config()
        self.client = Client(
            host=config["host"],
            port=config["port"],
            username=config["username"],
            password=config["password"]
        )

    def get_torrents(self) -> List[Torrent]:
        return self.client.get_torrents()
    
    def get_torrent(self, hash) -> Torrent:
        return self.client.get_torrent(torrent_id=hash)
    
    def add_torrent(self, url, dir) -> Torrent:
        return self.client.add_torrent(torrent=url, download_dir=dir)

    def remove_torrent(self, id) -> None:
        return self.client.remove_torrent(id, delete_data=False)

    def stop_torrent(self, id) -> None:
        return self.client.stop_torrent(id)
    
    def start_torrent(self, id) -> None:
        return self.client.start_torrent(id)