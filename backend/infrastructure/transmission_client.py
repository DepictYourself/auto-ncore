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

    def get_torrents(self, fields) -> List[Torrent]:
        return self.client.get_torrents(arguments=fields)
    
    def get_torrent(self, hash, fields) -> Torrent:
        return self.client.get_torrent(torrent_id=hash, arguments=fields)
    
    def add_torrent(self, url, dir) -> Torrent:
        return self.client.add_torrent(torrent=url, download_dir=dir)

    def remove_torrents(self, ids, remove_files) -> None:
        self.client.remove_torrent(ids=ids, delete_data=remove_files)

    def stop_torrents(self, ids) -> None:
        return self.client.stop_torrent(ids)
    
    def start_torrent(self, ids) -> None:
        return self.client.start_torrent(ids)