# app/main.py
"""
Main entry point for the FastAPI application.
This file sets up the FastAPI app and includes the resume feedback API.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import resume
from app.api import resume, recommendation

app.include_router(resume.router, prefix="/resume", tags=["Resume Feedback"])
app.include_router(recommendation.router, prefix="/career", tags=["Career Recommendation"])


app = FastAPI(
    title="AI-Powered Career Coach API",
    description="Provides resume feedback, job matching, and career guidance using LLMs",
    version="1.0.0"
)

# CORS (Optional for frontend/backend separation)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this in production!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(resume.router, prefix="/resume", tags=["Resume Feedback"])

@app.get("/", tags=["Health Check"])
def root():
    return {"message": "AI Career Coach API is running 🚀"}