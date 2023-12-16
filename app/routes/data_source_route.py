import logging
from typing import Any

from fastapi import APIRouter


from models.data_sources_model import DataSourcesModel
from services.google_drive_data_source_service import GoogleDriveDataSourceService
from services.text_splitter_service import TextSplitterService
from services.url_data_source_service import UrlDataSourceService
from services.vector_db_service import VectorDBService

data_sources_router = APIRouter(
    prefix='/data-sources'
)
logger = logging.getLogger(__name__)


@data_sources_router.post("/")
async def process_new_data_sources(data_sources_model: DataSourcesModel) -> dict[str, Any]:
    logger.info(f"Received data sources: URLs - {data_sources_model.urls}, "
                f"Google Drive IDs - {data_sources_model.gdrive_folder_ids}")

    gdrive_docs = GoogleDriveDataSourceService.load_docs_from_source_list(data_sources_model.gdrive_folder_ids)
    url_docs = UrlDataSourceService.load_docs_from_source_list(data_sources_model.urls)
    doc_splits = TextSplitterService().split_docs(gdrive_docs + url_docs)

    VectorDBService.add_docs(doc_splits)

    return {"message": "Data Sources List received", "data": data_sources_model}
