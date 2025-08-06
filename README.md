# 🧠 AI-Powered Career Coach

**“Intelligent Assistant for Career Growth”**

This is an end-to-end AI-powered assistant that helps job seekers and professionals get actionable career insights using modern LLMs and full-stack deployment.

---

## 🚀 Features

- ✍️ **Tailored Resume Feedback**  
- 📈 **Career Path Recommendation (based on skills/interests)**  
- 📋 **Job Description Summarization + profile alignment scoring(Fit Score)**  
- 🎤 **Mock Interview with AI**  
The system uses local models via LLaMA/Ollama and integrates modern tools like FastAPI, LangChain, Streamlit, Pinecone, and Docker, following a clean microservices architecture with optional Redis, PostgreSQL, and Kafka integrations.
---

## 🎯 Key Objectives
Build a modular, scalable, and production-ready AI career assistant

Use LLMs to simulate real-world feedback and conversations

Enable document embedding + retrieval with vector DBs

Provide an interactive UI using Streamlit or React

Deploy with Docker + CI/CD pipelines (Render, Railway, or AWS)
---
| Component         | Technology                            |
| ----------------- | ------------------------------------- |
| Language          | Python 3.11+                          |
| Backend API       | FastAPI                               |
| LLM Engine        | OpenAI GPT-4 / LLaMA via Ollama       |
| Prompt Management | LangChain                             |
| Frontend          | Streamlit                             |
| Cache Store       | Redis (optional)                      |
| Vector Database   | Pinecone / FAISS                      |
| SQL Database      | PostgreSQL (optional)                 |
| Messaging         | Apache Kafka (optional for async ops) |
| Containerization  | Docker, Docker Compose                |
| Monitoring        | Prometheus + Grafana (optional)       |

---

## Project Structure
``` career-coach-ai/
│
├── .env                  # API keys and config
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── LICENSE
├── README.md
├── requirements.txt
│
├── app/
│   ├── main.py                # FastAPI entry point
│   ├── api/                   # API routes
│   │   ├── resume.py
│   │   ├── recommendation.py
│   │   ├── jobmatch.py
│   │   └── interview.py
│   ├── services/              # Core logic
│   │   ├── llm_engine.py
│   │   ├── prompt_templates.py
│   │   ├── resume_feedback.py
│   │   ├── career_recommender.py
│   │   └── job_matcher.py
│   ├── vectorstore/
│   │   ├── pinecone_client.py
│   │   └── embed_jobs.py
│   ├── database/              # Optional SQL backend
│   │   ├── db.py
│   │   ├── models.py
│   │   └── queries.py
│   ├── cache/                 # Optional Redis
│   │   └── redis_client.py
│   ├── kafka/                 # Optional Kafka
│   │   ├── producer.py
│   │   └── consumer.py
│   └── config/
│       └── settings.py
│
├── frontend/
│   └── streamlit_app.py
│
├── data/
│   ├── resumes/
│   ├── job_descriptions/
│   └── embeddings/
│
├── notebooks/
│   └── prompt_tests.ipynb
│
└── tests/
    ├── test_resume.py
    ├── test_jobmatch.py
    └── test_api.py
```
---
## 🔧 Project Components
1️⃣ Resume Feedback System
Accepts resume text via frontend

Uses LLM to provide structured, section-by-section feedback

Optionally stores version history in PostgreSQL

2️⃣ Career Recommendation Engine
Collects user profile (skills, interests, background)

Matches with real-world career paths via LLM + embeddings

3️⃣ Job Description Matcher
Summarizes job description

Scores match between job and user resume

Stores top matches using Pinecone or FAISS

4️⃣ Mock Interview Module
Chat-based simulated interviews

Tailored to job roles or fields (e.g., Data Science, Software Engineering)

LLM-driven Q&A loop with rating feedback
---

## 📆 Timeline & Deliverables
📌 Milestone 1: Core Architecture
 FastAPI + Streamlit setup

 LLM integration (OpenAI / Ollama)

 Resume feedback module

 Pinecone vector search

 Docker containerization

📌 Milestone 2: Feature Expansion
 Job matching & summarization

 LangChain chaining logic

 Career path recommendation

 Redis caching & PostgreSQL integration

📌 Milestone 3: Finalization & Deployment
 Mock interview module

 Logging, monitoring with Prometheus/Grafana

 GitHub Actions for CI/CD

 Cloud deployment (Render or Railway)
---

## ⚙️ Running the Project
🔹 Local Development (Linux/Mac/Windows)
```bash
# Clone the repository
git clone https://github.com/yourusername/career-coach-ai.git
cd career-coach-ai

# Create virtual env
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run backend
uvicorn app.main:app --reload

# Run frontend
streamlit run frontend/streamlit_app.py
```
---

## Dockerized Run
docker-compose up --build
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
