# app/llm/model.py

"""Shared model loader using ChatOllama so both API and Streamlit use the same instance."""

from langchain_community.chat_models import ChatOllama

# Global singleton
_llm_instance = None

def get_model():
    """Returns the singleton ChatOllama instance."""
    global _llm_instance
    if _llm_instance is None:
        print("Loading ChatOllama model into memory... (only once)")
        _llm_instance = ChatOllama(
            model="llama2:7b",
            temperature=0.2
        )
    return _llm_instance

def warm_up():
    """Runs a small inference to avoid first-call delay."""
    llm = get_model()
    print("Warming up model...")
    try:
        _ = llm.invoke("Hello")
        print("Model warmed up and ready.")
    except Exception as e:
        print(f"Warm-up failed: {e}")