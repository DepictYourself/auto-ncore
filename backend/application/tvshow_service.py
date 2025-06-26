from infrastructure.config_service import ConfigService
from infrastructure.tmdb_client import TmdbClient

class TvShowService:
  def __init__(self):
    self.config = ConfigService()
    self.client = TmdbClient(self.config)

  def get_tvshow_details(self, id):
    return self.client.get_show_details(id)