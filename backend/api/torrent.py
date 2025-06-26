from fastapi import APIRouter, Response
from application.torrent_service import TorrentClientService
from api.dtos.add_torrent_request import AddTorrentRequest
from api.dtos.stop_torrents_request import StopTorrentsRequest
from api.dtos.start_torrents_request import StartTorrentsRequest
from api.dtos.delete_torrents_request import DeleteTorrentsRequest




router = APIRouter()
torrent_client_service = TorrentClientService()

@router.get('/')
def get_torrents() -> Response:
    return torrent_client_service.list_torrents()


@router.post('/download')
def add_torrent(dto: AddTorrentRequest) -> Response:
    return torrent_client_service.add_torrent(dto)
    


@router.get('/{hash_string}')
def get_torrent(hash_string: str) -> Response:
    torrent = torrent_client_service.get_torrent(hash_string)
    return {
        "id": torrent.id, "name": torrent.name, "progress": torrent.progress,
        "status": torrent.status
    }
    

@router.delete('/')
def remove_torrent(request: DeleteTorrentsRequest) -> Response:
    return torrent_client_service.remove_torrent(request.ids)
    


@router.post('/stop')
def stop_torrent(request: StopTorrentsRequest) -> Response:
    return torrent_client_service.stop_torrents(request.ids)
    
    

@router.post('/start')
def resume_torrent(req: StartTorrentsRequest) -> Response:
    return torrent_client_service.start_torrent(req.ids)



@router.get('/show_details/{show_id}')
def testtest(show_id: str) -> Response:
    return torrent_client_service.test_show_details(show_id)