import logging

from fastapi import APIRouter, HTTPException

from models.chat_message_model import ChatMessageModel
from services.agent_executor_service import AgentExecutorService

chat_router = APIRouter(prefix='/chat')
logger = logging.getLogger(__name__)


@chat_router.post("/query")
async def chat_query(chat_message: ChatMessageModel):
    logger.info(f"Received query: {chat_message.message}")
    try:
        agent_response = AgentExecutorService().execute(chat_message.message)
        return ChatMessageModel(message=agent_response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
