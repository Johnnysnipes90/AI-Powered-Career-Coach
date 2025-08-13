# frontend/streamlit_app.py

"""Streamlit frontend for AI-Powered Career Coach.
Provides a user-friendly interface for resume feedback and career recommendations.
"""

import streamlit as st
import requests
import json

def display_polished_feedback(intro, suggestions):
    """
    Display polished resume feedback in Streamlit.

    Parameters:
    - intro (str): A short introduction or summary feedback text.
    - suggestions (list): A list of individual suggestion strings.
    """
    if intro:
        st.markdown(f"### 📋 Overview")
        st.write(intro)

    if suggestions:
        st.markdown("### 💡 Suggestions for Improvement")
        for idx, suggestion in enumerate(suggestions, start=1):
            st.markdown(f"- **{idx}.** {suggestion}")
    else:
        st.info("No suggestions available.")




# -------------------------
# CONFIGURATION
# -------------------------
API_URL = "http://localhost:8000"

st.set_page_config(
    page_title="AI-Powered Career Coach",
    page_icon="🎯",
    layout="centered"
)

# Custom CSS for aesthetics
st.markdown("""
    <style>
    .stTextArea textarea {font-size: 15px;}
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        border-radius: 8px;
        padding: 0.5em 1em;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------
# TITLE & DESCRIPTION
# -------------------------
st.title("🎯 AI-Powered Career Coach")
st.markdown(
    "Get **personalized resume feedback** and **career recommendations** instantly."
    "\n\n_Powered by AI, designed to help you grow your career._"
)

# -------------------------
# FEATURE SELECTION
# -------------------------
section = st.radio(
    "Choose a feature:",
    ["📄 Resume Feedback", "💼 Career Recommendation"]
)

# -------------------------
# RESUME FEEDBACK SECTION
# -------------------------
if section == "📄 Resume Feedback":
    st.subheader("Choose how you want to provide your resume:")

    input_method = st.radio(
        "Select input method:",
        ["📂 Upload PDF", "✏️ Paste Text"]
    )

    if input_method == "📂 Upload PDF":
        uploaded_file = st.file_uploader("Upload your resume (PDF only):", type=["pdf"])

        if uploaded_file is not None:
            if st.button("🚀 Get Feedback"):
                with st.spinner("Analyzing your resume file..."):
                    try:
                        res = requests.post(
                            f"{API_URL}/resume-feedback",
                            files = {
                                "file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")
                            }
                        )
                        res.raise_for_status()
                        res_data = res.json()
                        intro = res_data.get("intro", "")
                        suggestions = res_data.get("suggestions", [])
                        st.success("✅ Feedback received!")

                        display_polished_feedback(intro, suggestions)
                    except requests.exceptions.RequestException as e:
                        st.error(f"API request failed: {e}")

    elif input_method == "✏️ Paste Text":
        resume_text = st.text_area("Paste your resume text here:")

        if resume_text.strip():
            if st.button("🚀 Get Feedback"):
                with st.spinner("Analyzing your pasted resume..."):
                    try:
                        res = requests.post(
                            f"{API_URL}/resume-feedback",
                            data={"resume_text": resume_text}
                        )
                        res.raise_for_status()
                        feedback_list = res.json().get("feedback", [])
                        st.success("✅ Feedback received!")

                        if feedback_list:
                            display_polished_feedback(feedback_list)
                        else:
                            st.info("No feedback returned.")
                    except requests.exceptions.RequestException as e:
                        st.error(f"API request failed: {e}")

# -------------------------
# CAREER RECOMMENDATION SECTION
# -------------------------
elif section == "💼 Career Recommendation":
    st.subheader("Tell Us About You")
    skills = st.text_area(
        "Enter your skills:",
        placeholder="e.g. Python, Data Analysis, Project Management..."
    )
    interests = st.text_area(
        "Enter your interests:",
        placeholder="e.g. Artificial Intelligence, Finance, Education..."
    )

    if st.button("📊 Get Career Recommendations"):
        if not skills.strip() or not interests.strip():
            st.error("Please enter both skills and interests.")
        else:
            with st.spinner("Generating recommendations..."):
                try:
                    res = requests.post(
                        f"{API_URL}/career-recommendation",
                        data={"skills": skills, "interests": interests}
                    )
                    res.raise_for_status()
                    recommendations = res.json().get("recommendations", [])
                    st.success("✅ Recommendations ready!")

                    if recommendations:
                        st.markdown("### Suggested Careers:")
                        st.markdown(recommendations)

                    else:
                        st.info("No recommendations found.")
                except requests.exceptions.RequestException as e:
                    st.error(f"API request failed: {e}")