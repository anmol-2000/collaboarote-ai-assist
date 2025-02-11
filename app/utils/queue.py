from celery import Celery
from app.utils.config import REDIS_URL
from app.utils.ai import analyze_code

celery_app = Celery("tasks", broker=REDIS_URL)

@celery_app.task
def analyze_code_task(code: str):
    return analyze_code(code)
