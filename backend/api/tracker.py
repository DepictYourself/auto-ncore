from fastapi import APIRouter, Response
from application.services import TrackerService
from domain.torrent_category import TorrentCategory

router = APIRouter()
tracker_client_service = TrackerService()


@router.get('/')
def list_rss():
    try:
        return tracker_client_service.list_torrents()
    except Exception as e:
        return { "error": str(e) }


@router.get('/search/{pattern}')
def search_ncore(pattern: str):
    try:
        return tracker_client_service.search_torrent(pattern, TorrentCategory.MOVIE)
    except Exception as e:
        return { "error": str(e)}
    

@router.get('/{ncore_id}')
def get_one(ncore_id):
    try:
        return tracker_client_service.get_details(ncore_id)
    except Exception as e:
        return { "error": str(e)}