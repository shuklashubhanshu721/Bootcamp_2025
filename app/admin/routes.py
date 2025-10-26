from fastapi import APIRouter

router = APIRouter()

@router.get("/status")
def admin_status():
    return {"module": "AdminModule", "status": "active"}