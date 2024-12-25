#! python3.11
import os
import time
from fastapi import FastAPI, Response
from transmission_rpc import Client


TRANSMISSION_HOST = os.getenv('TRANSMISSION_HOST', 'localhost')
TRANSMISSION_PORT = int(os.getenv('TRANSMISSION_PORT', 9091))
TRANSMISSION_USER = os.getenv('TRANSMISSION_USER')
TRANSMISSION_PASS = os.getenv('TRANSMISSION_PASS')
NCORE_KEY = os.getenv('NCORE_KEY')

client = Client(
    host=TRANSMISSION_HOST,
    port=TRANSMISSION_PORT,
    username=TRANSMISSION_USER,
    password=TRANSMISSION_PASS
)

app = FastAPI()


@app.get('/')
def read_root() -> Response:
    return Response("Ok.", media_type="text/html; charset=utf-8")


@app.get('/torrents')
def get_torrents() -> Response:
    return client.get_torrents()


@app.get('/torrents/{hash_string}')
def get_torrent(hash_string: str) -> Response:
    try:
        torrent = client.get_torrent(hash_string)
        return {
            "id": torrent.id, "name": torrent.name, "progress": torrent.progress,
            "status": torrent.status
        }
    except Exception as e:
        return {"error": str(e)}


@app.post('/torrents')
def add_torrent(url: str) -> Response:
    try:
        torrent = client.add_torrent(url)
        return { "message": "Torrent added successfully.", "torrent_id": torrent.id}
    except Exception as e:
        return { "error": str(e)}
    

@app.delete('/torrents/{hash_string}')
def remove_torrent(hash_string: str) -> Response:
    try:
        client.remove_torrent(hash_string, delete_data=False)
        return { "message": f"Torrent {hash_string} removed successfully."}
    except Exception as e:
        return { "error": str(e) }


@app.post('/torrents/{hash_string}/pause')
def pause_torrent(hash_string: str) -> Response:
    try:
        client.stop_torrent(hash_string)
        return {"message": f"Torrent {hash_string} paused successfully."}
    except Exception as e:
        return {"error": str(e)}
    

@app.post('/torrents/{hash_string}/resume')
def resume_torrent(hash_string: str) -> Response:
    try:
        client.start_torrent(hash_string)
        return {"message": f"Torrent {hash_string} resumed successfully."}
    except Exception as e:
        return {"error": str(e)}
