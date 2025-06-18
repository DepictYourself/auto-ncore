from typing import List
from pydantic import BaseModel


class DeleteTorrentsRequest(BaseModel):
  ids: List[int | str]