#! python3.11
from fastapi import FastAPI, Response
from api import movie, torrent, tracker


app = FastAPI()

# Include routers
app.include_router(torrent.router, prefix='/torrents', tags=["Torrent"])
app.include_router(tracker.router, prefix='/tracker', tags=["Tracker"])
app.include_router(movie.router, prefix='/movie', tags=["Movie"])


@app.get('/')
def read_root() -> Response:
    return Response("Ok.", media_type="text/html; charset=utf-8")
