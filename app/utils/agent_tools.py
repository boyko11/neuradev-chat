from langchain.tools.retriever import create_retriever_tool
from langchain_community.tools.ddg_search.tool import DuckDuckGoSearchResults
from langchain_community.utilities.google_search import GoogleSearchAPIWrapper
from langchain_community.utilities.google_serper import GoogleSerperAPIWrapper
from langchain_core.tools import Tool

from app.services.vector_db_service import VectorDBService

neuradev_rag_tool = create_retriever_tool(
    VectorDBService.db_as_retriever(),
    "neuradev-retriever",
    "Searches and returns documents regarding Neuradev",
)

duck_search = Tool(
    name="duck-search",
    func=DuckDuckGoSearchResults().run,
    description="duck-search to search with duckduckgo for questions related to the Neurodev.AI corporation. As such,"
                "the search term should always refer to the 'Neurodev.AI corporation'."
)

google_search_tool = Tool(
    name="google-search",
    description="google-search to search with google for questions related to the Neurodev.AI corporation. As such,"
                "the search term should always refer to the 'Neurodev.AI corporation'.",
    func=GoogleSearchAPIWrapper().run,
)


def pre_format_google_serper(query):
    google_serper_query = query.replace("Neuradev", "Neuradev.AI Corporation California")
    print(f'google_serper_query: {google_serper_query}')
    return GoogleSerperAPIWrapper().run(google_serper_query)


google_serper_tool = Tool(
    name="google-serper",
    description="google-serper to search with google for questions related to the Neurodev.AI corporation.",
    func=pre_format_google_serper
)
