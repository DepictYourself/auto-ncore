from typing import List
from transmission_rpc import Client, Torrent

class TransmissionClient:
    def __init__(self, host, port, username, password):
        self.client = Client(host=host, port=port, username=username, password=password)

    def get_torrents(self) -> List[Torrent]:
        return self.client.get_torrents()
    
    def get_torrent(self, id) -> Torrent:
        return self.client.get_torrent(id)
    
    def add_torrent(self, url, dir) -> Torrent:
        return self.client.add_torrent(torrent=url, download_dir=dir)

    def remove_torrent(self, id) -> None:
        return self.client.remove_torrent(id, delete_data=False)

    def stop_torrent(self, id) -> None:
        return self.client.stop_torrent(id)
    
    def start_torrent(self, id) -> None:
        return self.client.start_torrent(id)