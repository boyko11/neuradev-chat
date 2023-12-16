from pydantic import BaseModel, HttpUrl
from typing import List


class DataSourcesModel(BaseModel):
    urls: List[HttpUrl]
    gdrive_folder_ids: List[str]
