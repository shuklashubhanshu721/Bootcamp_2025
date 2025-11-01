# Bootcamp 2025 – Full Stack Project

This repository contains the complete implementation for the **Itrade Bootcamp 2025** project — a modular full-stack system designed to demonstrate backend microservices and a modern frontend framework.

---

## 🧱 Project Overview

The project is divided into two main components:

1. **Backend (FastAPI)** — provides modular REST API services.
2. **Frontend (Next.js + TypeScript)** — provides a modern UI powered by React and Shadcn/UI components.

This architecture supports scalability, modular separation, and clear service boundaries between feature modules like **Auth**, **Admin**, **Knowledge**, **Queries**, and **Feedback**.

---

## ⚙️ Tech Stack

### **Frontend**
- [Next.js 14+](https://nextjs.org/)
- TypeScript
- Tailwind CSS
- Shadcn/UI component system
- Node.js 20.9.0 (required)

### **Backend**
- [FastAPI](https://fastapi.tiangolo.com/)
- Python 3.10+
- MongoDB Atlas (via `pymongo`)
- Dotenv-based configuration
- Modular route system

---

## 🚀 Running the Application

### 🖥️ Prerequisites
Make sure you have the following installed:
- **Node.js v20.9.0 or higher** (`nvm install 20.9.0`)
- **Python 3.10+**
- **MongoDB connection string** set in `.env`

### 🔹 Backend Setup

```bash
cd app
python3 -m venv venv
source venv/bin/activate
pip install -r ../requirements.txt
uvicorn main:app --reload
```

The backend server will start at:
> http://127.0.0.1:8000

You can check API docs at:
> http://127.0.0.1:8000/docs

---

### 🔹 Frontend Setup

```bash
cd frontend
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
nvm use 20.9.0
npm install
npm run dev
```

Access the frontend at:
> http://localhost:3000

---

## 🧩 Project Modules

**Backend Modules:**
- `auth` – User authentication and session handling
- `query` – Query management logic
- `feedback` – Feedback collection endpoints
- `knowledge` – Knowledge base services
- `admin` – Admin and data management endpoints

**Frontend Modules:**
- `src/app` – Application routes and layout
- `src/components` – UI components (Button, Card, Input)
- `src/lib` – Utility libraries and helpers

---

## 🧰 Environment Variables

Create a `.env` file at the project root or within `/app` containing:

```
DATABASE_URL=<your_mongodb_connection_string>
SECRET_KEY=<fastapi_secret_key>
```

---

## 🧠 Development Notes

- Always run the backend in a virtual environment.
- Before running frontend commands, ensure Node 20.9.0 is selected via nvm.
- Use `requirements.txt` for dependency version consistency.
- Ensure both frontend and backend are active for full functionality.

---

## 📦 Deployment Notes

After local testing is complete:
1. Commit all sprint changes using the provided sprint commit template.
2. Push to the sprint branch.
3. Delegate deployment to the **Infra Architect mode** to publish:
   - Frontend → Vercel  
   - Backend → Render

---

**Maintainer:** Shubhanshus  
© 2025 Itrade Bootcamp