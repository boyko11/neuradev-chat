from langchain.tools.retriever import create_retriever_tool
from langchain_community.tools.ddg_search.tool import DuckDuckGoSearchResults
from langchain_community.utilities.google_serper import GoogleSerperAPIWrapper
from langchain_core.tools import Tool

from config.config import ToolsConfig
from services.vector_db_service import VectorDBService

def get_enabled_tools():

    enabled_tools = []

    if ToolsConfig.RAG_ENABLED:
        neuradev_rag_tool = create_retriever_tool(
            VectorDBService.db_as_retriever(),
            "neuradev-retriever",
            "Searches and returns documents regarding Neuradev",
        )
        enabled_tools.append(neuradev_rag_tool)

    if ToolsConfig.GOOGLE_SERPER_ENABLED:
        def pre_format_google_serper(query):
            google_serper_query = query.replace("Neuradev", "Neuradev.AI Corporation California")
            print(f'google_serper_query: {google_serper_query}')
            return GoogleSerperAPIWrapper().run(google_serper_query)

        google_serper_tool = Tool(
            name="google-serper",
            description="google-serper to search with google for questions related to the Neurodev.AI corporation.",
            func=pre_format_google_serper
        )
        enabled_tools.append(google_serper_tool)

    if ToolsConfig.DUCK_SEARCH_ENABLED:
        duck_search = Tool(
            name="duck-search",
            func=DuckDuckGoSearchResults().run,
            description="duck-search to search with duckduckgo for questions related to the Neurodev.AI corporation. As such,"
                        "the search term should always refer to the 'Neurodev.AI corporation'."
        )
        enabled_tools.append(duck_search)

    if ToolsConfig.GOOGLE_SEARCH_ENABLED:
        google_search = Tool(
            name="google-search",
            func=GoogleSerperAPIWrapper().run,
            description="google-search to search with google for questions related to the Neurodev.AI corporation. As such,"
                        "the search term should always refer to the 'Neurodev.AI corporation'."
        )
        enabled_tools.append(google_search)

    return enabled_tools
