from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.db.db_session import SessionLocal
from app.db.models import CodeFile
from pydantic import BaseModel

router = APIRouter()

class CodeFileCreate(BaseModel):
    filename: str
    content: str

@router.post("/")
def create_code_file(code_file: CodeFileCreate, db: Session = SessionLocal()):
    db_code_file = CodeFile(filename=code_file.filename, content=code_file.content)
    db.add(db_code_file)
    db.commit()
    return db_code_file
