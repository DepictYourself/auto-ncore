
from api.request import TorrentDTO
from domain.torrent_category import TorrentCategory
from infrastructure.config_service import ConfigService
from infrastructure.ncore_client import NCoreClient
from infrastructure.transmission_client import TransmissionClient
from infrastructure.kodi_directory_mapper import KodiDirectoryMapper
from infrastructure.tmdb_client import TmdbClient


class TorrentClientService:
    def __init__(self):
        self.config_service = ConfigService()
        self.client = TransmissionClient(self.config_service)
        self.ncore_client = NCoreClient(self.config_service)
        self.tmdb_client = TmdbClient(self.config_service)
        self.kodi_dir_mapper = KodiDirectoryMapper(self.config_service)

    def list_torrents(self):
        return self.client.get_torrents()
    
    def torrent_info(self, id: int | str):
        return self.client.get_torrent(id)
    
    def add_torrent(self, torrent: TorrentDTO):
        print("services.py add_torrent() called.")
        category = self.kodi_dir_mapper.map_category(type=torrent.type)
        print("category: ", category)
        
        download_dir = self.config_service.get_tranmission_config()['dir']
        subdir = "/"
        if(category == TorrentCategory.SHOW):
            tmdb_result = self.tmdb_client.search_show(torrent.title)
            print("tmdb_result: ", tmdb_result)
            show_name = ""
            release_year = ""
            season_number = 0
            subdir += self.kodi_dir_mapper.get_tvshow_directory(
                show_name,
                release_year,
                season_number
            )
        elif(category == TorrentCategory.MOVIE):
            subdir += "movies/"

        download_dir += subdir
        url = torrent.download

        #return self.client.add_torrent(url, dir=download_dir)
    

    def remove_torrent(self, id: int | str):
        return self.client.remove_torrent(id)
    
    def stop_torrent(self, id: int | str):
        return self.client.stop_torrent(id)
    
    def start_torrent(self, id: int | str):
        return self.client.start_torrent(id)
    
    def test_tmdb(self, query):
        return self.tmdb_client.search_show(query)
    
    def test_show_details(self, tmdb_id):
        return self.tmdb_client.get_show_details(tmdb_id)
    

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
    
    def shows(self, title: str):
        return self.client.parse_tvshow_title(title)