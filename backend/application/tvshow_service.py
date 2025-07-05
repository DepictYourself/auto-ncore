from typing import List
from models.tmdb import TmdbTvShow
from infrastructure.config_service import ConfigService
from infrastructure.tmdb_client import TmdbClient

class TvShowService:
  def __init__(self):
    self.config = ConfigService()
    self.client = TmdbClient(self.config)

  def discover(self) -> List[TmdbTvShow]:
    results = self.client.discover_tvshows(without_genres="10767")["results"]
    return results

  def get_tvshow_details(self, id):
    return self.client.get_show_details(id)