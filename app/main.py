from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


import logging

from routes.chat_route import chat_router
from routes.data_source_route import data_sources_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allows the frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO)

app.include_router(data_sources_router)
app.include_router(chat_router)



@app.get("/")
async def welcome():
    return {"message": "Welcome to the Neuradev Chat app! Live Long and Prosper!"}
