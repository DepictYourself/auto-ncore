from pydantic import BaseModel, Field, HttpUrl
from typing import Literal

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