from typing import List
from pydantic import BaseModel


class StartTorrentsRequest(BaseModel):
  ids: List[int | str]