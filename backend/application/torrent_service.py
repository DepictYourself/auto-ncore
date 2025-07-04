from typing import List
from urllib.parse import parse_qs
from domain.torrent_category import TorrentCategory
from infrastructure.config_service import ConfigService
from infrastructure.ncore_client import NCoreClient
from infrastructure.transmission_client import TransmissionClient
from infrastructure.kodi_directory_mapper import KodiDirectoryMapper
from infrastructure.tmdb_client import TmdbClient
from api.dtos.add_torrent_request import AddTorrentRequest


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
    
    def add_torrent(self, request: AddTorrentRequest):
        id = parse_qs(request.url.query)["id"][0]
        torrent = self.ncore_client.get_torrent_info(id)
        category = self.kodi_dir_mapper.map_category(type=torrent["type"].value)
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

        return self.client.add_torrent(str(request.url), dir=download_dir)
      

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
    


    

