from typing import Optional
import requests
from infrastructure.config_service import ConfigService
from models.tmdb import (
    TmdbMovieDetails,
    tmdb_discover_movie_response,
    TmdbTVSearchResponse,
    TmdbTVShowDetails,
    SortBy,
    tmdb_discover_tvshow_response,
)


class TmdbClient:
    def __init__(self, config_service: ConfigService):
        self.config = config_service.get_tmdb_config()

    def _get_headers(self):
        return {
            "Authorization": f"Bearer {self.config['jwt']}",
            "Content-Type": "application/json;charset=utf-8",
            "Accept": "application/json",
        }

    def discover_movies(
        self,
        adult: bool = False,
        include_video: bool = False,
        language: str = "en-US",
        page: int = 1,
        sort_by: SortBy = SortBy.popularity_desc,
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
                "sort_by": sort_by,
            },
            headers=headers,
        )
        if response.status_code != 200:
            raise Exception(
                f"Failed to fetch tmdb api /discover/movie endpoint: {response.text}"
            )
        return response.json()

    def discover_tvshows(
        self,
        language: str = "en-US",
        sort_by: str = "popularity.desc",
        page: int = 1,
        timezone: Optional[str] = None,
        air_date_gte: Optional[str] = None,
        air_date_lte: Optional[str] = None,
        first_air_date_year: Optional[int] = None,
        first_air_date_gte: Optional[str] = None,
        first_air_date_lte: Optional[str] = None,
        vote_average_gte: Optional[float] = None,
        vote_average_lte: Optional[float] = None,
        vote_count_gte: Optional[int] = None,
        vote_count_lte: Optional[int] = None,
        with_genres: Optional[str] = None,
        with_watch_providers: Optional[str] = None,
        watch_region: Optional[str] = None,
        with_original_language: Optional[str] = None,
        with_runtime_gte: Optional[int] = None,
        with_runtime_lte: Optional[int] = None,
        include_adult: bool = False,
        include_null_first_air_dates: bool = False,
        without_genres: Optional[str] = None,
    ) -> tmdb_discover_tvshow_response:
        base_url = self.config["url"]
        headers = self._get_headers()
        params = {
            "language": language,
            "sort_by": sort_by,
            "page": page,
            "include_adult": str(include_adult).lower(),
            "include_null_first_air_dates": str(include_null_first_air_dates).lower(),
        }

        # Add only if not None
        optional_params = {
            "timezone": timezone,
            "air_date.gte": air_date_gte,
            "air_date.lte": air_date_lte,
            "first_air_date_year": first_air_date_year,
            "first_air_date.gte": first_air_date_gte,
            "first_air_date.lte": first_air_date_lte,
            "vote_average.gte": vote_average_gte,
            "vote_average.lte": vote_average_lte,
            "vote_count.gte": vote_count_gte,
            "vote_count.lte": vote_count_lte,
            "with_genres": with_genres,
            "with_watch_providers": with_watch_providers,
            "watch_region": watch_region,
            "with_original_language": with_original_language,
            "with_runtime.gte": with_runtime_gte,
            "with_runtime.lte": with_runtime_lte,
            "without_genres": without_genres
        }
        for key, value in optional_params.items():
            if value is not None:
                params[key] = value
        
        response = requests.get(
            base_url + "/discover/tv",
            params=params,
            headers=headers
        )
        print(f"discover_tvshows() response: ", response.)
        if response.status_code != 200:
            raise Exception(
                f"Failed to fetch tmdb api /discover/tv endpoint: {response.text}"
            )
        return response.json()


    def search_show(
        self, query_string, include_adult=False, language="en-US", result_page=1
    ) -> TmdbTVSearchResponse:
        url = self.config["url"]
        headers = self._get_headers()
        response = requests.get(
            url + "/search/tv",
            params={
                "query": query_string,
                "include_adult": include_adult,
                "language": language,
                "page": result_page,
            },
            headers=headers,
        )
        return response.json()

    def get_show_details(self, id, language="en-US") -> TmdbTVShowDetails:
        url = self.config["url"]
        response = requests.get(
            url + f"/tv/{id}",
            params={"language": language},
            headers=self._get_headers(),
        )
        return response.json()

    def get_movie_details(self, id, language="en-US") -> TmdbMovieDetails:
        url = self.config["url"] + f"/movie/{id}?language={language}"
        headers = self._get_headers()
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise Exception(response.json())
        return response.json()
