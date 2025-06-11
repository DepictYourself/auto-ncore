from fastapi import APIRouter, Response
from application.services import TorrentClientService
from api.request import TorrentDTO




router = APIRouter()
torrent_client_service = TorrentClientService()

@router.get('/')
def get_torrents() -> Response:
    return torrent_client_service.list_torrents()


@router.post('/download')
def add_torrent(dto: TorrentDTO) -> Response:
    try:
        torrent = torrent_client_service.add_torrent(dto)
        return { "message": "Torrent added successfully.", "torrent_id": torrent.id}
    except Exception as e:
        return { "error": str(e)}


@router.get('/{hash_string}')
def get_torrent(hash_string: str) -> Response:
    try:
        torrent = torrent_client_service.get_torrent(hash_string)
        return {
            "id": torrent.id, "name": torrent.name, "progress": torrent.progress,
            "status": torrent.status
        }
    except Exception as e:
        return {"error": str(e)}
    

@router.delete('/{hash_string}')
def remove_torrent(hash_string: str) -> Response:
    try:
        torrent_client_service.remove_torrent(hash_string)
        return { "message": f"Torrent {hash_string} removed successfully."}
    except Exception as e:
        return { "error": str(e) }


@router.post('/{hash_string}/pause')
def pause_torrent(hash_string: str) -> Response:
    try:
        torrent_client_service.stop_torrent(hash_string)
        return {"message": f"Torrent {hash_string} paused successfully."}
    except Exception as e:
        return {"error": str(e)}
    

@router.post('/{hash_string}/resume')
def resume_torrent(hash_string: str) -> Response:
    try:
        torrent_client_service.start_torrent(hash_string)
        return {"message": f"Torrent {hash_string} resumed successfully."}
    except Exception as e:
        return {"error": str(e)}


@router.get('/test/{query_string}')
def test(query_string: str) -> Response:
    return torrent_client_service.test_tmdb(query_string)


@router.get('/show_details/{show_id}')
def testtest(show_id: str) -> Response:
    return torrent_client_service.test_show_details(show_id)