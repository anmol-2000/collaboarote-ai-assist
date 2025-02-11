from fastapi import APIRouter
from app.utils.queue import analyze_code_task

router = APIRouter()

@router.post("/analyze/")
def analyze_code_endpoint(code: str):
    task = analyze_code_task.delay(code)
    return {"task_id": task.id}
