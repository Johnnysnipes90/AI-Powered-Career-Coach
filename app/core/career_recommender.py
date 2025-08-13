# app/core/career_recommender.py

"""This module provides functionality to recommend careers based on skills and interests using an LLM chain."""

from app.llm.chains import career_recommendation_chain

def recommend_career(skills, interests):
    try:
        rec_list = career_recommendation_chain(skills, interests)
        return {"recommendations": rec_list}
    except Exception as e:
        return {
            "error": f"LLM processing failed: {str(e)}",
            "recommendations": []
        }
