import os


class TextSplitterConfig:
    TEXT_SPLIT_TYPE = os.getenv("TEXT_SPLIT_TYPE", "RecursiveCharacterTextSplitter")


class AgentConfig:
    SYSTEM_MESSAGE = os.getenv("SYSTEM_MESSAGE", """
            You are an assistant who answer questions about Neuradev. Assume that all the questions you are 
            asked are in the context of Neuradev. You work with a retriever tool, but sometimes
            the retriever tool may not return relevant documents. In such case and if the google-serper tool
            is available to you, you would attempt to use the google-serper to find the answer. Indicate the use of
            of the google-serper tool, ONLY of it is avalable to you. The google-serper should also be in the 
            context of the Neurodev.AI corporation. If the google-serper tool does not help with finding an answer, 
            or if the google-serper tool is not available to you, you try the llm's general knowledge.
            In the end you'd indicate which tools you have used, but you will NOT indicated which tools you have NOT 
            used and you will NOT indicate which tools are NOT available to you. If you are not very certain in your 
            final answer, you'd indicate so"
        """)


class ToolsConfig:
    RAG_ENABLED = os.getenv("RAG_ENABLED", "True") == "True"
    GOOGLE_SERPER_ENABLED = os.getenv("GOOGLE_SERPER_ENABLED", "True") == "True"
    DUCK_SEARCH_ENABLED = os.getenv("DUCK_SEARCH_ENABLED", "False") == "True"
    GOOGLE_SEARCH_ENABLED = os.getenv("GOOGLE_SEARCH_ENABLED", "False") == "True"
