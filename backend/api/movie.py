from fastapi import APIRouter, Response
from application.services import MovieService


router = APIRouter()
movie_service = MovieService()

@router.get('/discover')
def get_torrents() -> Response:
    return movie_service.discover_movies()
    