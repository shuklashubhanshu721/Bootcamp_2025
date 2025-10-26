from fastapi import APIRouter

router = APIRouter()

@router.get("/status")
def knowledge_status():
    return {"module": "KnowledgeModule", "status": "active"}