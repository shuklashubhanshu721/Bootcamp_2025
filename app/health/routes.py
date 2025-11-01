from fastapi import APIRouter
from app.infrastructure.database.mongo_client import client

router = APIRouter(prefix="/api/v1", tags=["health"])


@router.get("/health")
async def health_check():
    try:
        # Attempt to retrieve MongoDB server info
        client.server_info()
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}