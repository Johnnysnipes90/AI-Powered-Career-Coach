import streamlit as st
import requests

st.set_page_config(page_title="AI Career Coach", page_icon="🧠")

st.title("🧠 AI-Powered Career Coach")
st.markdown("Get instant feedback on your resume using a local LLaMA-3 model.")

# Resume form
with st.form("resume_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    resume_text = st.text_area("Paste Your Resume Text", height=300)

    submitted = st.form_submit_button("Get Feedback")

if submitted:
    if not resume_text.strip():
        st.warning("Please paste your resume text.")
    else:
        with st.spinner("Analyzing your resume..."):
            try:
                response = requests.post(
                    "http://localhost:8000/resume/feedback",
                    json={
                        "name": name,
                        "email": email,
                        "resume_text": resume_text
                    },
                    timeout=30
                )
                if response.status_code == 200:
                    data = response.json()
                    st.success("✅ Feedback Received!")

                    st.subheader("Summary:")
                    st.write(data["feedback_summary"])

                    st.subheader("Suggestions:")
                    for s in data["suggestions"]:
                        st.markdown(f"- {s}")
                else:
                    st.error(f"❌ Error: {response.json()['detail']}")

            except Exception as e:
                st.error(f"💥 Exception: {str(e)}")