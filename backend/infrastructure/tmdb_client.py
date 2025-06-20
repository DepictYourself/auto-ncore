import requests
from infrastructure.config_service import ConfigService
from models.tmdb import TmdbMovieDetails, tmdb_discover_movie_response, TmdbTVSearchResponse, TmdbTVShowDetails, SortBy


class TmdbClient:
    def __init__(self, config_service: ConfigService):
        self.config = config_service.get_tmdb_config()


    def _get_headers(self):
        return {
            "Authorization": f"Bearer {self.config['jwt']}",
            "Content-Type": "application/json;charset=utf-8",
            "Accept": "application/json"
        }

    
    def discover_movies(
            self,
            adult: bool = False,
            include_video: bool = False,
            language: str = "en-US",
            page: int = 1,
            sort_by: SortBy = SortBy.popularity_desc
        ) -> tmdb_discover_movie_response:
        # The discover request can be extended with more params
        base_url = self.config["url"]
        headers = self._get_headers()
        response = requests.get(
            base_url + "/discover/movie",
            params={
                "include_adulst": adult,
                "include_video": include_video,
                "language": language,
                "page": page,
                "sort_by": sort_by
            },
            headers=headers
        )
        if(response.status_code != 200):
            raise Exception(f"Failed to fetch tmdb api /discover/movie endpoint: {response.text}")
        return response.json()
    

    def search_show(
            self,
            query_string,
            include_adult=False,
            language="en-US",
            result_page=1
    ) -> TmdbTVSearchResponse:
        url = self.config["url"]
        headers = self._get_headers()
        response = requests.get(
            url+"/search/tv",
            params={
                "query":query_string,
                "include_adult": include_adult,
                "language": language,
                "page": result_page
            },
            headers=headers
        )
        return response.json()
    

    def get_show_details(self, id, language="en-US") -> TmdbTVShowDetails:
        url = self.config["url"]
        response = requests.get(
            url+f"/tv/{id}",
            params={
                "language": language
            },
            headers=self._get_headers()
        )
        return response.json()
    

    def get_movie_details(self, id, language="en-US") -> TmdbMovieDetails:
        url = self.config["url"] + f"/movie/{id}?language={language}"
        headers = self._get_headers()
        response = requests.get(url, headers=headers)
        if( not response.ok):
            raise Exception(response.json())
        return response.json()
