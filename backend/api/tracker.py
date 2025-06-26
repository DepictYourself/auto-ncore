from fastapi import APIRouter
from application.tracker_service import TrackerService
from domain.torrent_category import TorrentCategory

router = APIRouter()
tracker_client_service = TrackerService()


@router.get('/')
def list_rss():
    return tracker_client_service.list_torrents()


@router.get('/search/{pattern}')
def search_ncore(pattern: str):
    return tracker_client_service.search_torrent(pattern, TorrentCategory.MOVIE)
    

@router.get('/{ncore_id}')
def get_one(ncore_id):
    return tracker_client_service.get_details(ncore_id)