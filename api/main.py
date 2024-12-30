#! python3.11
import os
from fastapi import FastAPI, Response

from application.services import TorrentService

from infrastructure.transmission_client import TransmissionClient


NCORE_KEY = os.getenv('NCORE_KEY')
NCORE_USER = os.getenv('NCORE_USER')
NCORE_PASS = os.getenv('NCORE_PASS')

app = FastAPI()


client = TransmissionClient(
    host=os.getenv('TRANSMISSION_HOST', 'localhost'),
    port=int(os.getenv('TRANSMISSION_PORT', 9091)),
    username=os.getenv('TRANSMISSION_USER'),
    password=os.getenv('TRANSMISSION_PASS')
)

service = TorrentService(client)


@app.get('/')
def read_root() -> Response:
    return Response("Ok.", media_type="text/html; charset=utf-8")


@app.get('/torrents')
def get_torrents() -> Response:
    return service.list_torrents()


@app.get('/torrents/{hash_string}')
def get_torrent(hash_string: str) -> Response:
    try:
        torrent = service.get_torrent(hash_string)
        return {
            "id": torrent.id, "name": torrent.name, "progress": torrent.progress,
            "status": torrent.status
        }
    except Exception as e:
        return {"error": str(e)}


@app.post('/torrents')
def add_torrent(url: str) -> Response:
    try:
        torrent = service.add_torrent()
        return { "message": "Torrent added successfully.", "torrent_id": torrent.id}
    except Exception as e:
        return { "error": str(e)}
    

@app.delete('/torrents/{hash_string}')
def remove_torrent(hash_string: str) -> Response:
    try:
        service.remove_torrent(hash_string)
        return { "message": f"Torrent {hash_string} removed successfully."}
    except Exception as e:
        return { "error": str(e) }


@app.post('/torrents/{hash_string}/pause')
def pause_torrent(hash_string: str) -> Response:
    try:
        service.stop_torrent(hash_string)
        return {"message": f"Torrent {hash_string} paused successfully."}
    except Exception as e:
        return {"error": str(e)}
    

@app.post('/torrents/{hash_string}/resume')
def resume_torrent(hash_string: str) -> Response:
    try:
        service.start_torrent(hash_string)
        return {"message": f"Torrent {hash_string} resumed successfully."}
    except Exception as e:
        return {"error": str(e)}
