from typing import List
from api.dtos.torrent_dto import TorrentDTO
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
        fields = [
          "id",
          "hashString",
          "name",
          "addedDate",
          "percentDone",
          "status",
          "downloadDir",
          "totalSize",
          "downloadEver",
          "uploadRation",
          "peersConnected"
          "magnetLink",
        ]
        return self.client.get_torrents(fields)
    
    def get_torrent(self, hash: str):
        fields = [
          "id",
          "hashString",
          "name",
          "addedDate",
          "percentDone",
          "status",
          "downloadDir",
          "totalSize",
          "downloadEver",
          "uploadRation",
          "peersConnected"
          "magnetLink",
        ]
        return self.client.get_torrent(hash, fields)
    
    def add_torrent(self, torrent: TorrentDTO):
        category = self.kodi_dir_mapper.map_category(type=torrent.type)
        print("add_torrent()", torrent_title_info)
        download_dir = self.config_service.get_tranmission_config()['dir']
        subdir = "/"
        if(category == TorrentCategory.SHOW):
            show_title = self.ncore_client.parse_tvshow_title(torrent.title)
            torrent_title_info = self.ncore_client.extract_season_episode(torrent.title)
            
            tmdb_result = self.tmdb_client.search_show(show_title)
            tmdb_result.results.__len__
            if tmdb_result.total_results == 1:
                tmdb_id = tmdb_result.results[0].id
                show_details = self.tmdb_client.get_show_details(tmdb_id)
                show_name = show_details.name
                release_year = show_details.first_air_date[0:5]
                season_number = torrent_title_info[1]
                # subdir += self.kodi_dir_mapper.get_tvshow_directory(
                #     show_name,
                #     release_year,
                #     season_number
                # )
        elif(category == TorrentCategory.MOVIE):
            subdir += "movies/"

        download_dir += subdir
        url = torrent.download

        #return self.client.add_torrent(url, dir=download_dir)
      

    def remove_torrent(self, ids: List[int | str]):
        torrents = []
        for id in ids:
            torrent = self.get_torrent(id)
            torrents.append(torrent)
        
        remove_files = True
        self.client.remove_torrents(ids, remove_files)
        return {"message": f"Torrents removed successfully. {ids}"}
    

    def stop_torrents(self, ids: List[int | str]):
      self.client.stop_torrents(ids)
      return f"Successfully stopped torrents {ids}"
          
    
    def start_torrent(self, ids: List[int | str]):
        self.client.start_torrent(ids)
        return {"message": f"Torrents started successfully {ids}"}
    
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
    

class MovieService:
    def __init__(self):
        self.config_service = ConfigService()
        self.client = TmdbClient(self.config_service)

    def discover_movies(self):
        results = self.client.discover_movies(adult=False, include_video=False, page=1)["results"]
        return results