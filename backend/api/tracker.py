from fastapi import APIRouter, Response
from application.services import TrackerService
from domain.torrent_category import TorrentCategory

router = APIRouter()
tracker_client_service = TrackerService()


@router.get('/search/{pattern}')
def search_ncore(pattern: str):
    try:
        return tracker_client_service.search_torrent(pattern, TorrentCategory.MOVIE)
    except Exception as e:
        return { "error": str(e)}