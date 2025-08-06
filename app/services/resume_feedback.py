import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"  # Make sure this matches your pulled model

def get_resume_feedback(resume_text: str) -> dict:
    prompt = f"""
You are a professional career coach. Given the resume text below, return:

1. A short summary of strengths and weaknesses.
2. A bullet list of 4–5 improvement suggestions.

Resume:
{resume_text}
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

        # Simple parsing – adjust to your LLaMA output
        lines = result.strip().split("\n")
        summary = lines[0]
        suggestions = [line for line in lines[1:] if line.strip().startswith("-")]

        return {
            "summary": summary.strip(),
            "suggestions": suggestions or ["Improve resume formatting", "Tailor to specific job roles"]
        }

    except Exception as e:
        raise RuntimeError(f"Error getting response from Ollama: {e}")