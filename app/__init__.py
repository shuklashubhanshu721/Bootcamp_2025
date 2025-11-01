# Bootcamp_2025 Application Initialization
# This file initializes the FastAPI application modules

from fastapi import FastAPI
from app.auth.routes import router as auth_router
from app.query.routes import router as query_router
from app.feedback.routes import router as feedback_router
from app.knowledge.routes import router as knowledge_router
from app.admin.routes import router as admin_router

app = FastAPI(title="Bootcamp_2025 Backend API")

# Enable CORS
from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Routers
app.include_router(auth_router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(query_router, prefix="/api/v1/query", tags=["Queries"])
app.include_router(feedback_router, prefix="/api/v1/feedback", tags=["Feedback"])
app.include_router(knowledge_router, prefix="/api/v1/knowledge", tags=["Knowledge"])
app.include_router(admin_router, prefix="/api/v1/admin", tags=["Admin"])

@app.get("/")
def root():
    return {"message": "Bootcamp_2025 API is running successfully"}