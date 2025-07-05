from fastapi import APIRouter, Response

from application.tvshow_service import TvShowService


router = APIRouter()
tvshow_service = TvShowService()


@router.get('/discover')
def discover_tvshows() -> Response:
    return tvshow_service.discover()


@router.get('/{tmdb_id}')
def get_movie_details(tmdb_id: int) -> Response:
    return tvshow_service.get_movie_details(tmdb_id)