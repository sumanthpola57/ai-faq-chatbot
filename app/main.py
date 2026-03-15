from fastapi import FastAPI
from app.api.chat_routes import router

app = FastAPI(title="Smart FAQ Chatbot")

app.include_router(router)

@app.get("/")
def home():
    return {"message": "FAQ Chatbot running"}