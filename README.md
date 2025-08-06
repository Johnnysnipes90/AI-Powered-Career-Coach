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
| Docker & Docker-compose      | Containerization |
| Dependency Management	| uv |
| Render / Railway | Deployment |

---

## 🗂️ Project Structure

```
AI-Powered-Career-Coach/
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

## 📦 Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/Johnnysnipes90/AI-Powered-Career-Coach.git
cd AI-Powered-Career-Coach
```
### 2. Create virtual environment & install dependencies
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
uv pip install -r requirements.txt
```
### 3. Run FastAPI Backend
```bash
uvicorn app.main:app --reload
```
### 4. Run Streamlit Frontend
```bash
streamlit run frontend/streamlit_app.py
```
### 5. 📦 Docker
```bash
docker-compose up --build
```
### 🔒 API Keys
```bash
OPENAI_API_KEY=your-openai-key
PINECONE_API_KEY=your-pinecone-key
```
---
## 📜 License
MIT License
---

## 👨‍💻 Author
Olalemi John Oluwatosin
📧 johnolalemi90@gmail.com
🔗 LinkedIn
🔗 GitHub
