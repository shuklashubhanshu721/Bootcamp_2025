# Bootcamp_2025 Application Initialization
# This file initializes the FastAPI application modules

from fastapi import FastAPI
from app.auth.routes import router as auth_router
from app.query.routes import router as query_router
from app.feedback.routes import router as feedback_router
from app.knowledge.routes import router as knowledge_router
from app.admin.routes import router as admin_router

app = FastAPI(title="Bootcamp_2025 Backend API")

# Register Routers
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(query_router, prefix="/query", tags=["Queries"])
app.include_router(feedback_router, prefix="/feedback", tags=["Feedback"])
app.include_router(knowledge_router, prefix="/knowledge", tags=["Knowledge"])
app.include_router(admin_router, prefix="/admin", tags=["Admin"])

@app.get("/")
def root():
    return {"message": "Bootcamp_2025 API is running successfully"}