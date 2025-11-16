from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.services.lupin_agent import LupinAgent
import json

router = APIRouter()

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    message: str
    history: Optional[List[Message]] = []

class ChatResponse(BaseModel):
    response: str
    role: str = "assistant"

@router.post("/lupin/stream")
async def chat_with_lupin_stream(request: ChatRequest, db: AsyncSession = Depends(get_db)):
    """
    Chat with Lupin with real-time streaming via Server-Sent Events
    """
    agent = LupinAgent(db)

    async def event_generator():
        try:
            async for event in agent.run(request.message):
                yield f"data: {json.dumps(event)}\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'type': 'error', 'content': str(e)})}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        }
    )

@router.post("/lupin", response_model=ChatResponse)
async def chat_with_lupin(request: ChatRequest, db: AsyncSession = Depends(get_db)):
    """
    Chat with Lupin (non-streaming fallback)
    """
    agent = LupinAgent(db)

    final_response = ""
    async for event in agent.run(request.message, max_iterations=10):
        if event.get("type") == "final":
            final_response = event.get("content", "")
            break
        elif event.get("type") == "error":
            raise HTTPException(status_code=500, detail=event.get("content"))

    if not final_response:
        final_response = "I'm working on your request. This may take a moment..."

    return ChatResponse(
        response=final_response,
        role="assistant"
    )

@router.get("/health")
async def chat_health():
    return {"status": "Chat router is healthy"}
