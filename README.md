# Url and Google Drive ChatBot

## Introduction

This chatbot web application is designed to answer questions based on content from websites and Google Drive folders. It's built with **React**, **Python**, **FastAPI**, **LangChain**, and **"Open"AI's GPT models**.

### Application Flow:

1. **URLs and Google Drive Folders**: Start by entering a list of URLs and Google Drive folder IDs.
2. **Document Creation**:
   - **URLs**: LangChain's [UnstructuredURLLoader](https://python.langchain.com/docs/integrations/document_loaders/url) converts the list of URLs into documents.
   - **Google Drive**: LangChain's [GoogleDriveLoader](https://python.langchain.com/docs/integrations/document_loaders/google_drive) processes the Google Drive folder IDs into documents.
3. **Document Splitting**: LangChain's [RecursiveCharacterTextSplitter](https://python.langchain.com/docs/integrations/text_splitters/recursive_character_text_splitter) splits the documents into chunks (default size of 2000 chars and overlap of 300 chars).
4. **Embedding Generation**: Converts splits into 1536 dimensional embeddings using LangChain's [OpenAIEmbeddings](https://python.langchain.com/docs/integrations/text_embedding/openai) with the text-embedding-ada-002 model.
5. **Vector Store**: Stores the embeddings with their corresponding text in a [FAISS](https://python.langchain.com/docs/integrations/vectorstores/faiss) vector store.
6. **Retriever Tool**: The vector db is used as a "retriever tool"
7. **Google Search Tool**: Utilizes [Serper](https://serper.dev/) for web searches.
8. **Conversational Agent**: LangChain's [Conversational_Retrieval_Agent](https://python.langchain.com/docs/use_cases/question_answering/conversational_retrieval_agents) uses the above tools to answer queries.
   - First, it searches for relevant information in the retriever tool.
   - If unsuccessful, it resorts to the Google search tool.
   - If still unsuccessful, it relies on the general knowledge of GPT-4.
9. **Contextual Conversations**: Maintains a generous conversation history window of 20000 tokens to leverage the context in ongoing conversations.
10. **AgentConfig**: The current "system_message" is configured for Neuradev.ai. You could configure the Agent's system_message to your needs by setting the env variable **SYSTEM_MESSAGE**

This workflow should result a responsive and knowledgeable chatbot.

## Prerequisites

Before you start, ensure you have the following:

- Python 3.11 or higher.
- pip
- [OpenAI API key](https://platform.openai.com/api-keys).
- [OpenAI API Credits](https://platform.openai.com/account/billing/overview) (Required for API calls).
- [Google Serper API key](https://serper.dev/api-key).
- [LangChain Google Drive Prerequisites](https://python.langchain.com/docs/integrations/document_loaders/google_drive) (For Google Drive integration).

## Installation

### Local Setup

#### Installing Dependencies

```bash
pip install -r requirements.txt
```

#### Running the Backend App

Inside the `app` directory:

```bash
cd app
OPENAI_API_KEY={your_open_api_key} GOOGLE_APPLICATION_CREDENTIALS={path to credentials.json} SERPER_API_KEY={your_serper_api_key} uvicorn main:app --reload
```

#### Running the Frontend App

Inside the `react-app` directory:

```bash
cd react-app
npm install  # only once to install dependencies
npm start
```

### Docker Setup (using docker-compose)

#### Build Images

```bash
docker-compose build
```

#### Run Containers

```bash
OPENAI_API_KEY={your_open_api_key} GOOGLE_APPLICATION_CREDENTIALS={path to credentials.json} SERPER_API_KEY={your_serper_api_key} docker-compose up
```

## Accessing the App

Once the app is running, you can access it at:

```
http://localhost:3000
```

Enter your URLs and Google Drive Folder IDs, save them, and chat away with the data they contain.

## Note on Docker Setup

The LangChain Google Drive Loader requires a browser installed inside the container. The current Docker image setup does not support this, meaning you won't be able to use Google Drive in the Docker environment due to errors. The local setup outside of Docker works fine for Google Drive integration.
