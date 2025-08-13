# app/llm/chains.py
"""
LLM chains for AI-Powered Career Coach.
Uses a CPU-friendly model for fast responses,
and defines prompt chains for resume feedback and career recommendations.
"""

from langchain.prompts import ChatPromptTemplate
from app.llm.model import get_model



def resume_feedback_chain(resume_text: str):
    llm = get_model()

    prompt = ChatPromptTemplate.from_template("""
        You are a career coach reviewing a resume.

        First, provide a short 1–2 sentence introduction summarizing your overall impression.
        Do NOT number or bullet this introduction.

        Then, list exactly five actionable improvement suggestions for the resume.
        Rules:
        1. Format suggestions as a clean numbered list starting at 1.
        2. Each suggestion must be a single concise sentence in a polished, professional tone.
        3. Avoid repetition.
        4. Do NOT add any extra commentary before or after the list.

        Resume:
        {resume_text}

        Output format:
        [Introduction sentence(s)]

        1. First suggestion
        2. Second suggestion
        3. Third suggestion
        4. Fourth suggestion
        5. Fifth suggestion
    """)

    messages = prompt.format_messages(resume_text=resume_text)
    response = llm.invoke(messages)
    raw_output = response.content.strip()

    lines = [line.strip() for line in raw_output.splitlines() if line.strip()]

    intro_lines = []
    suggestion_lines = []

    for line in lines:
        if line.lstrip().startswith(("1.", "1)")):
            suggestion_lines.append(line)
        elif suggestion_lines:
            suggestion_lines.append(line)
        else:
            intro_lines.append(line)

    intro_text = " ".join(intro_lines).rstrip(".") + "."

    cleaned_suggestions = [
        line.lstrip("1234567890.) ").strip().rstrip(".") + "."
        for line in suggestion_lines
    ][:5]

    while len(cleaned_suggestions) < 5:
        cleaned_suggestions.append("Additional feedback not provided.")

    return {
        "intro": intro_text,
        "suggestions": cleaned_suggestions
    }


def career_recommendation_chain(skills: str, interests: str):
    llm = get_model()

    prompt = ChatPromptTemplate.from_template("""
        You are a professional career advisor.
        Based on the following skills and interests, suggest exactly three career paths 
        in a numbered list format.

        For each career path:
        1. **Bold** the career name.
        2. Write a single short summary line.
        3. Add bullet points for:
           • Key Tasks (2–3 tasks)
           • Why It Fits You (one sentence linking user's skills/interests)

        Format example:
        1. **Data Scientist**  
        Works with data to uncover insights and build predictive models.  
        - **Key Tasks:** Analyze datasets, build models, communicate findings  
        - **Why It Fits You:** Strong analytical skills align with your interests.

        Skills: {skills}
        Interests: {interests}
    """)

    messages = prompt.format_messages(skills=skills, interests=interests)
    response = llm.invoke(messages)
    return response.content.strip()