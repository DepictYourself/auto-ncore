from infrastructure.config_service import ConfigService
from infrastructure.tmdb_client import TmdbClient


class MovieService:
    def __init__(self):
        self.config_service = ConfigService()
        self.client = TmdbClient(self.config_service)

    def discover_movies(self):
        results = self.client.discover_movies(adult=False, include_video=False, page=1)["results"]
        return results
    

    def get_movie_details(self, tmdb_id: int):
        results = self.client.get_movie_details(tmdb_id)
        return results