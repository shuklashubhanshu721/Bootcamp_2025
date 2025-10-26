from fastapi import APIRouter

router = APIRouter()

@router.get("/status")
def feedback_status():
    return {"module": "FeedbackModule", "status": "active"}