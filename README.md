# 🧠 AI-Powered Career Coach

**“Intelligent Assistant for Career Growth”**

This is an end-to-end AI-powered assistant that helps job seekers and professionals get actionable career insights using modern LLMs and full-stack deployment.

---

## 🚀 Features

- ✍️ **Tailored Resume Feedback**  
- 📈 **Career Path Recommendation** (based on skills/interests)  
- 📋 **Job Description Summarization + Fit Score**  
- 🎤 **Mock Interview with AI**  

The system uses local models via **LLaMA/Ollama** and integrates modern tools like **FastAPI**, **LangChain**, **Streamlit**, **Pinecone**, and **Docker**, following a clean microservices architecture with optional Redis, PostgreSQL, and Kafka integrations.

---

## 🎯 Key Objectives

- Build a modular, scalable, and production-ready AI career assistant  
- Use LLMs to simulate real-world feedback and conversations  
- Enable document embedding + retrieval with vector DBs  
- Provide an interactive UI using Streamlit or React  
- Deploy with Docker + CI/CD pipelines (Render, Railway, or AWS)  

---

## 🛠 Tech Stack

| Component         | Technology                            |
|------------------|----------------------------------------|
| Language          | Python 3.11+                           |
| Backend API       | FastAPI                                |
| LLM Engine        | OpenAI GPT-4 / LLaMA via Ollama        |
| Prompt Management | LangChain                              |
| Frontend          | Streamlit                              |
| Cache Store       | Redis *(optional)*                     |
| Vector Database   | Pinecone / FAISS                       |
| SQL Database      | PostgreSQL *(optional)*                |
| Messaging         | Apache Kafka *(optional)*              |
| Containerization  | Docker, Docker Compose                 |
| Monitoring        | Prometheus + Grafana *(optional)*      |

---

## 📂 Project Structure

```bash
AI-Powered-Career-Coach/
├── .env
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── LICENSE
├── README.md
├── requirements.txt
│
├── app/
│   ├── main.py
│   ├── api/
│   │   ├── resume.py
│   │   ├── recommendation.py
│   │   ├── jobmatch.py
│   │   └── interview.py
│   ├── services/
│   │   ├── llm_engine.py
│   │   ├── prompt_templates.py
│   │   ├── resume_feedback.py
│   │   ├── career_recommender.py
│   │   └── job_matcher.py
│   ├── vectorstore/
│   │   ├── pinecone_client.py
│   │   └── embed_jobs.py
│   ├── database/
│   │   ├── db.py
│   │   ├── models.py
│   │   └── queries.py
│   ├── cache/
│   │   └── redis_client.py
│   ├── kafka/
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

### 🔧 Project Components
1️⃣ Resume Feedback System
Accepts resume text via frontend

Uses LLM to provide structured, section-by-section feedback

Optionally stores version history in PostgreSQL

2️⃣ Career Recommendation Engine
Collects user profile (skills, interests, background)

Matches with real-world career paths via LLM + embeddings

3️⃣ Job Description Matcher
Summarizes job descriptions

Scores alignment with user resume

Stores top matches using Pinecone/FAISS

4️⃣ Mock Interview Module
Simulated interviews via chat

Tailored to roles (e.g., Data Science, Backend Dev)

LLM-driven Q&A + performance rating
---

## 📆 Timeline & Deliverables
📌 Milestone 1: Core Architecture
FastAPI + Streamlit setup

LLM integration (OpenAI/Ollama)

Resume feedback module

Pinecone vector search

Docker containerization

📌 Milestone 2: Feature Expansion
Job matching & summarization

LangChain chaining logic

Career recommendation

Redis + PostgreSQL integration

📌 Milestone 3: Finalization & Deployment
Mock interview module

Logging, monitoring with Prometheus/Grafana

GitHub Actions CI/CD

Cloud deployment (Render, Railway, or AWS)
---

## ⚙️ Running the Project
🔹 Local Development
```bash
# Clone the repo
git clone https://github.com/Johnnysnipes90/AI-Powered-Career-Coach.git
cd AI-Powered-Career-Coach

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run FastAPI backend
uvicorn app.main:app --reload

# Run Streamlit frontend
streamlit run frontend/streamlit_app.py
```
---

## 🐳 Dockerized Run
```
docker-compose up --build
```
---
## 🔒 Environment Variables
Create a .env
```
OPENAI_API_KEY=your-openai-key
PINECONE_API_KEY=your-pinecone-key
```
---
## 📝 API Endpoints (Planned)
🔹 Resume
| Method | Endpoint         | Description                 |
| ------ | ---------------- | --------------------------- |
| POST   | /resume/feedback | Get resume improvement tips |
| GET    | /resume/{id}     | Retrieve feedback summary   |

🔹 Job Matching
| POST | /job/match | Match resume to job ad |
| POST | /job/summarize | Summarize job description |

🔹 Career Recommendation
| POST | /career/recommend | Suggest career paths |

🔹 Mock Interview
| POST | /interview/start | Start mock interview |
| POST | /interview/answer | Submit answer for feedback |
---

## 👨‍💻 Author
Olalemi John Oluwatosin
📧 johnolalemi90@gmail.com
🔗 LinkedIn: www.linkedin.com/in/john-olalemi
🔗 GitHub: github.com/Johnnysnipes90