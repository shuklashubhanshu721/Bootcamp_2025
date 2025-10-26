from fastapi import APIRouter

router = APIRouter()

@router.get("/status")
def auth_status():
    return {"module": "AuthModule", "status": "active"}