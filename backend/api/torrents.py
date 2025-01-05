from typing import Literal
from fastapi import APIRouter, Response
from pydantic import BaseModel, Field, HttpUrl
from application.services import TorrentClientService

class TorrentDTO(BaseModel):
    id: str
    title: str
    key: str

    class Size(BaseModel):
        _unit: Literal["GiB", "MiB", "KiB"]
        _size: float

    size: Size
    type: str
    date: str
    seed: int = Field(..., ge=0)
    leech: int = Field(..., ge=0)
    download: HttpUrl
    url: HttpUrl


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
