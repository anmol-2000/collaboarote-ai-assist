from fastapi import FastAPI
from app.api_router import auth, code_files, websocket, assist
from app.db.db_session import engine, Base

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include API routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(code_files.router, prefix="/code", tags=["Code Files"])
app.include_router(websocket.router, prefix="/ws", tags=["WebSocket"])
app.include_router(assist.router, prefix="/assist", tags=["AI"])
