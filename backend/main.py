#! python3.11
from fastapi import FastAPI, Response
from api import torrents, tracker


app = FastAPI()

# Include routers
app.include_router(torrents.router, prefix='/torrents', tags=["Torrents"])
app.include_router(tracker.router, prefix='/tracker', tags=["Tracker"])


@app.get('/')
def read_root() -> Response:
    return Response("Ok.", media_type="text/html; charset=utf-8")
