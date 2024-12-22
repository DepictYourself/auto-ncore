#! python3.11
import os
import time
from fastapi import FastAPI, Response
from transmission_rpc import Client


TRANSMISSION_HOST = os.getenv('TRANSMISSION_HOST', 'localhost')
TRANSMISSION_PORT = int(os.getenv('TRANSMISSION_PORT', 9091))
TRANSMISSION_USER = os.getenv('TRANSMISSION_USER')
TRANSMISSION_PASS = os.getenv('TRANSMISSION_PASS')

print('torrent host: ', TRANSMISSION_HOST)
print('torrent port: ', TRANSMISSION_PORT)
print('torrent user: ', TRANSMISSION_USER)
print('torrent pw: ', TRANSMISSION_PASS)

client = Client(
    host=TRANSMISSION_HOST,
    port=TRANSMISSION_PORT,
    username=TRANSMISSION_USER,
    password=TRANSMISSION_PASS
)

app = FastAPI()


@app.get('/')
def read_root() -> Response:
    return Response("The server is running.")


@app.get('/torrents')
def get_torrents() -> Response:
    return client.get_torrents()
