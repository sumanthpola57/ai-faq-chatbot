from fastapi import APIRouter
from app.models.schemas import ChatRequest
from app.services.llm_service import generate_answer

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):

    answer = generate_answer(
        request.session_id,
        request.question
    )

    return {
        "session_id": request.session_id,
        "answer": answer
    }