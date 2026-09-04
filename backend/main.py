from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import httpx
import os
import json
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://ai-chat-application-frontend-iota.vercel.app", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

AI_API_URL = os.getenv("AI_API_URL")
AI_API_KEY = os.getenv("AI_API_KEY")

class ChatRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=1000, description="The user's question to the AI model.")


class ChatResponse(BaseModel):
    answer: str 

@app.get("/")
async def root():
    return {
        "message": "AI Chat Backend is running"
    }

@app.post("/api/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    if not AI_API_URL or not AI_API_KEY:
        raise HTTPException(status_code=500, detail="AI API URL or API Key is not configured. API credentials missing.")

    headers = {
        "x-api-key": AI_API_KEY,
        "Content-Type": "application/json"
    }

    external_payload = {
        "question": request.question
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(AI_API_URL, json=external_payload, headers=headers, timeout=10.0)
            response.raise_for_status()

            data = response.json()

            body_data = json.loads(data.get("body", "{}"))
            ai_anwser = body_data.get("answer", "no response received.")

            return ChatResponse(answer=ai_anwser)
        except httpx.TimeoutException:
            raise HTTPException(status_code=504, detail="External API timed out. Please try again.")
        
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail="Error communicating with AI service.")
        
        except Exception:
            raise HTTPException(status_code=500, detail="An unexpected internal server error occurred.")