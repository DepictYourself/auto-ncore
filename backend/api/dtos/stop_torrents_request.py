from typing import List
from pydantic import BaseModel


class StopTorrentsRequest(BaseModel):
  ids: List[int | str]