#! python3.11
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from api import movie, torrent, tracker


app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://192.168.0.2:85",
    "http://localhost:85",
    "http://asus:85"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Include routers
app.include_router(torrent.router, prefix='/torrents', tags=["Torrent"])
app.include_router(tracker.router, prefix='/tracker', tags=["Tracker"])
app.include_router(movie.router, prefix='/movie', tags=["Movie"])


@app.get('/')
def read_root() -> Response:
    return Response("Ok.", media_type="text/html; charset=utf-8")
