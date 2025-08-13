# app/core/resume_feedback.py
from app.utils.parser import extract_text_from_pdf
from app.llm.chains import resume_feedback_chain
from io import BytesIO

def get_resume_feedback(input_data):
    if hasattr(input_data, "file"):  
        text = extract_text_from_pdf(input_data)
    elif isinstance(input_data, str):
        text = input_data.strip()
    else:
        return {"intro": "", "suggestions": ["Invalid input."]}

    if not text:
        return {"intro": "", "suggestions": ["No readable content found in resume."]}

    return resume_feedback_chain(text)
