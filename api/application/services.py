from infrastructure.transmission_client import TransmissionClient
from infrastructure.kodi_directory_mapper import KodiDirectoryMapper


class TorrentService:
    def __init__(self, client: TransmissionClient):
        self.client = client

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

        return self.client.add_torrent(url, dir=download_dir)
    

    def remove_torrent(self, id: int | str):
        return self.client.remove_torrent(id)
    
    def stop_torrent(self, id: int | str):
        return self.client.stop_torrent(id)
    
    def start_torrent(self, id: int | str):
        return self.client.start_torrent(id)