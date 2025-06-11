from enum import Enum
from pydantic import BaseModel
from typing import List,Optional


class Genre(BaseModel):
    id: int
    name: str


class Network(BaseModel):
    id: int
    logo_path: Optional[str]
    name: str
    origin_country: str


class ProductionCompany(BaseModel):
    id: int
    logo_path: Optional[str]
    name: str
    origin_country: str


class Season(BaseModel):
    air_date: Optional[str]
    episode_count: int
    id: int
    name: str
    overview: str
    poster_path: Optional[str]
    season_number: int
    vote_average: float


class SpokenLanguage(BaseModel):
    english_name: str
    iso_639_1: str
    name: str


class Episode(BaseModel):
    id: int
    name: str
    overview: str
    vote_average: float
    vote_count: int
    air_date: Optional[str]
    episode_number: int
    episode_type: Optional[str]
    production_code: str
    runtime: Optional[int]
    season_number: int
    show_id: int
    still_path: Optional[str]


class TmdbTVShowDetails(BaseModel):
    adult: bool
    backdrop_path: Optional[str]
    created_by: List  # Can be detailed further if needed
    episode_run_time: List[int]
    first_air_date: Optional[str]
    genres: List[Genre]
    homepage: Optional[str]
    id: int
    in_production: bool
    languages: List[str]
    last_air_date: Optional[str]
    last_episode_to_air: Optional[Episode]
    name: str
    next_episode_to_air: Optional[Episode]
    networks: List[Network]
    number_of_episodes: int
    number_of_seasons: int
    origin_country: List[str]
    original_language: str
    original_name: str
    overview: str
    popularity: float
    poster_path: Optional[str]
    production_companies: List[ProductionCompany]
    production_countries: List  # Empty in your sample; define if used later
    seasons: List[Season]
    spoken_languages: List[SpokenLanguage]
    status: str
    tagline: Optional[str]
    type: str
    vote_average: float
    vote_count: int


class TmdbTVShow(BaseModel):
    adult: Optional[bool] = None
    backdrop_path: Optional[str] = None
    genre_ids: List[int]
    id: int
    origin_country: List[str]
    original_language: str
    original_name: str
    overview: str
    popularity: float = 0.0
    poster_path: Optional[str] = None
    first_air_date: Optional[str] = None
    name: str
    vote_average: float = 0.0
    vote_count: int = 0


class TmdbTVSearchResponse(BaseModel):
    page: int = 0
    results: List[TmdbTVShow]
    total_pages: int = 0
    total_results: int = 0


class TmdbMovie(BaseModel):
    adult: bool
    backdrop_path: str
    genre_ids: List[int]
    id: int
    original_language: str
    original_title: str
    overview: str
    popularity: float
    poster_path: str
    release_date: str
    title: str
    video: bool
    vote_average: float
    vote_count: int


class tmdb_discover_movie_response(BaseModel):
    page: int
    results: List[TmdbMovie]
    total_pages: int
    total_results: int


class SortBy(Enum):
    original_title_asc = "original_title.asc"
    original_title_desc = "original_title.desc"
    popularity_asc= "popularity.asc"
    popularity_desc = "popularity.desc"
    revenue_asc = "revenue.asc"
    revenue_desc = "revenue.desc"
    primary_release_date_asc = "primary_release_date.asc"
    primary_release_date_desc = "primary_release_date.desc"
    title_asc = "title.asc"
    title_desc = "title.desc"
    vote_avarage_asc = "vote_avarage.asc"
    vote_avarage_desc = "vote_avarage.desc"
    vote_count_asc = "vote_count.asc"
    vote_count_desc = "vote_count.desc"
