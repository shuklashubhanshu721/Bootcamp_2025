from fastapi import APIRouter

router = APIRouter()

@router.get("/status")
def query_status():
    return {"module": "QueryModule", "status": "active"}