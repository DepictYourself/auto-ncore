from fastapi import APIRouter, Response
from application.services import MovieService


router = APIRouter()
movie_service = MovieService()


@router.get('/discover')
def get_torrents() -> Response:
    return movie_service.discover_movies()


@router.get('/{tmdb_id}')
def get_movie_details(tmdb_id: int) -> Response:
    return movie_service.get_movie_details(tmdb_id)