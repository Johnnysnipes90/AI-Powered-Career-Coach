# app/services/career_recommender.py

"""
Service to recommend career paths based on user input.
Uses LLaMA via Ollama for inference.
"""

import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"

def recommend_career(skills: str, interests: str, background: str) -> str:
    prompt = f"""
You are a career advisor AI. Given the following user input, recommend 2–3 relevant career paths and briefly explain why.

Skills:
{skills}

Interests:
{interests}

Background:
{background}

Return a short paragraph summary and a bullet list of careers with explanation.
"""

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        result = response.json()["response"]
        return result.strip()
    except Exception as e:
        raise RuntimeError(f"Career recommendation failed: {e}")
