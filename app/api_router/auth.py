from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.db.db_session import SessionLocal
from app.db.models import User
from app.utils.security import hash_password, verify_password, create_jwt_token
from pydantic import BaseModel

router = APIRouter()

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

@router.post("/register")
def register(user: UserCreate, db: Session = SessionLocal()):
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already exists")
    
    hashed_pw = hash_password(user.password)
    db_user = User(username=user.username, email=user.email, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    return {"message": "User registered successfully"}

@router.post("/login")
def login(username: str, password: str, db: Session = SessionLocal()):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    token = create_jwt_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
