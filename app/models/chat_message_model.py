from pydantic import BaseModel


class ChatMessageModel(BaseModel):
    message: str