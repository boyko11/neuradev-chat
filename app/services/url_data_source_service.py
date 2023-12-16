import logging
from typing import List

from langchain_community.document_loaders import GoogleDriveLoader, UnstructuredURLLoader
from langchain_core.documents import Document

from app.services.abstract_source_list_doc_loader import AbstractSourceListDocLoader

logger = logging.getLogger(__name__)


class UrlDataSourceService(AbstractSourceListDocLoader):

    @staticmethod
    def load_docs_from_source_list(url_list: List[str]) -> List[Document]:

        loader = UnstructuredURLLoader(urls=url_list)
        docs = loader.load()

        logger.info(f'Num of total self: {len(docs)}')
        return docs
