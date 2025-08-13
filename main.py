# main.py

"""This file serves as the entry point for the FastAPI application.
It initializes the FastAPI app and includes the API router.
"""

"""FastAPI backend for AI-Powered Career Coach.
Serves endpoints for resume feedback and career recommendations.
"""

import logging
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.api.endpoints import router as api_router
from app.llm.model import warm_up

# -------------------------
# LOGGING CONFIGURATION
# -------------------------
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# -------------------------
# APP INITIALIZATION
# -------------------------
app = FastAPI(
    title="AI-Powered Career Coach",
    description="Provides AI-driven resume feedback and career recommendations.",
    version="1.0.0"
)

# -------------------------
# STARTUP EVENT
# -------------------------
@app.on_event("startup")
async def startup_event():
    logger.info("🚀 Application startup initiated...")
    try:
        logger.info("Warming up the model...")
        warm_up()
        logger.info("✅ Model warmed up successfully.")
    except Exception as e:
        logger.exception("❌ Model warm-up failed.")
        raise RuntimeError("Model initialization failed") from e

# -------------------------
# SHUTDOWN EVENT
# -------------------------
@app.on_event("shutdown")
async def shutdown_event():
    logger.info("🛑 Application shutdown.")

# -------------------------
# ERROR HANDLER
# -------------------------
@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    logger.error(f"Unhandled error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"message": "An unexpected error occurred. Please try again later."}
    )

# -------------------------
# ROUTES
# -------------------------
app.include_router(api_router)