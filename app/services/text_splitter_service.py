from config.config import TextSplitterConfig
from services.recursive_character_text_splitter_service import RecursiveCharacterTextSplitterService


class TextSplitterService:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(TextSplitterService, cls).__new__(cls)
            cls._instance.initialize(*args, **kwargs)
        return cls._instance

    def initialize(self, *args, **kwargs):

        if TextSplitterConfig.TEXT_SPLIT_TYPE == "RecursiveCharacterTextSplitter":
            self.splitter = RecursiveCharacterTextSplitterService()
        # elif TextSplitterConfig.TEXT_SPLIT_TYPE == "SomethingElse":
        #     self.splitter = SomethingElse()
        #     Add more conditions here for different configs

        if self.splitter is None:
            raise ValueError(f"Unknown text splitter type: {TextSplitterConfig.TEXT_SPLIT_TYPE}")

    def split_docs(self, docs):
        return self.splitter.split_docs(docs)


