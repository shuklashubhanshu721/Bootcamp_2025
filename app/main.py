from fastapi import FastAPI
from app.auth.routes import router as auth_router
from app.query.routes import router as query_router
from app.feedback.routes import router as feedback_router
from app.knowledge.routes import router as knowledge_router
from app.admin.routes import router as admin_router
from app.health.routes import router as health_router

from app import app as main_app

app = main_app

@app.get("/")
def read_root():
    return {"message": "Bootcamp_2025 API is running successfully"}