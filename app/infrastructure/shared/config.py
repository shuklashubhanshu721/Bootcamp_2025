import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Bootcamp_2025 Backend"
    environment: str = os.getenv("ENVIRONMENT", "development")
    database_url: str = os.getenv("DATABASE_URL", "mongodb://localhost:27017/bootcamp_2025")
    llm_api_url: str = os.getenv("LLM_API_URL", "https://api.openai.com/v1/chat/completions")
    llm_api_key: str = os.getenv("LLM_API_KEY", "")
    jwt_secret: str = os.getenv("JWT_SECRET", "supersecret")

settings = Settings()