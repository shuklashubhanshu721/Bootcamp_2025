# Bootcamp_2025 Backend

## Overview
This is the backend for the **Bootcamp_2025** project built using **FastAPI**. It provides the API layer for the application and is configured for deployment on **Render**.

---

## Project Structure
```
Bootcamp_2025/
├── app/
│   ├── __init__.py
│   └── main.py
├── requirements.txt
├── render.yaml
└── README.md
```

---

## Getting Started

### 1. Setup Virtual Environment
```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Development Server
```bash
uvicorn app.main:app --reload
```
Access the server at [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Deployment

The included `render.yaml` ensures Render detects the configuration automatically for deployment.

*Render service details:*
- Language: **Python**
- Framework: **FastAPI**
- Start command: `uvicorn app.main:app --host 0.0.0.0 --port 10000`
- Plan: **Free tier**

This setup eliminates the “No render.yaml found on main branch” error during deployment.