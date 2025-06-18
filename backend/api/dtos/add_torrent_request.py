from pydantic import BaseModel, HttpUrl

class AddTorrentRequest(BaseModel):
    url: HttpUrl
    tmdbId: str

