# app/api/resume.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.resume_feedback import get_resume_feedback

router = APIRouter()

class ResumeRequest(BaseModel):
    name: str
    email: str
    resume_text: str

class ResumeResponse(BaseModel):
    feedback_summary: str
    suggestions: list[str]

@router.post("/feedback", response_model=ResumeResponse)
def resume_feedback(payload: ResumeRequest):
    try:
        feedback = get_resume_feedback(payload.resume_text)
        return {
            "feedback_summary": feedback["summary"],
            "suggestions": feedback["suggestions"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))