# app/api/endpoints.py

from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse
from typing import Optional
from app.core.resume_feedback import get_resume_feedback
from app.core.career_recommender import recommend_career

router = APIRouter()

@router.post("/resume-feedback")
async def resume_feedback(
    file: Optional[UploadFile] = File(None),
    resume_text: Optional[str] = Form(None)
):
    """
    Accepts either an uploaded resume file (preferred) or raw text.
    File takes priority if both are provided.
    """
    try:
        if file is not None:
            feedback_result = get_resume_feedback(file)
        elif resume_text and resume_text.strip():
            feedback_result = get_resume_feedback(resume_text)
        else:
            return JSONResponse(
                status_code=400,
                content={"error": "Please upload a PDF or provide resume text."}
            )

        return JSONResponse(content=feedback_result)

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"Error processing resume: {str(e)}"}
        )


@router.post("/career-recommendation")
async def career_recommendation(
    skills: str = Form(...),
    interests: str = Form(...)
):
    """
    Generates career recommendations based on provided skills and interests.
    """
    try:
        if not skills.strip() or not interests.strip():
            return JSONResponse(
                status_code=400,
                content={"error": "Please provide both skills and interests."}
            )

        rec_result = recommend_career(skills, interests)
        return JSONResponse(content=rec_result)

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"Error generating career recommendation: {str(e)}"}
        )
