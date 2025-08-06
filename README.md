# 🧠 AI-Powered Career Coach

**“Intelligent Assistant for Career Growth”**

This is an end-to-end AI-powered assistant that helps job seekers and professionals get actionable career insights using modern LLMs and full-stack deployment.

---

## 🚀 Features

- ✍️ **Tailored Resume Feedback**  
- 📈 **Career Path Recommendation (based on skills/interests)**  
- 📋 **Job Description Summarization + Fit Score**  
- 🎤 **Mock Interview with AI**  

---

## 🛠️ Tech Stack

| Tool         | Purpose |
|--------------|---------|
| OpenAI / LLaMA | Natural Language Understanding |
| LangChain    | Prompt Chaining, LLM Orchestration |
| FastAPI      | Backend API for endpoints |
| Streamlit    | Frontend interface |
| Pinecone     | Vector DB for search |
| Docker       | Containerization |
| Render / Railway | Deployment |

---

## 🗂️ Project Structure

```
career-coach-ai/
│
├── .gitignore
├── README.md
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── LICENSE
│
├── app/
│   ├── main.py              # FastAPI app entry point
│   ├── api/                 # All API endpoints
│   │   ├── resume.py
│   │   ├── recommendation.py
│   │   ├── interview.py
│   │   └── summary.py
│   ├── services/            # Business logic
│   │   ├── llm_engine.py
│   │   ├── embeddings.py
│   │   ├── feedback.py
│   │   └── match_score.py
│   └── utils/               # Utility functions
│       └── helpers.py
│
├── frontend/
│   └── streamlit_app.py     # Streamlit UI logic
│
├── vectorstore/
│   ├── pinecone_client.py   # Connect to Pinecone
│   └── seed_data.py         # Upload resumes/job ads
│
├── data/
│   ├── resumes/
│   ├── job_descriptions/
│   └── examples/
│
├── notebooks/
│   └── llm_prompt_testing.ipynb
│
└── tests/
    ├── test_resume.py
    ├── test_recommendation.py
    └── test_api.py
```
---
