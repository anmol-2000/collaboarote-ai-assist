# Real-Time Collaborative Code Editor with AI-Assisted Debugging

This project provides a **FastAPI-based real-time code editor** with **AI-assisted debugging**. Users can edit code collaboratively, and AI-powered debugging suggestions are provided.

## Features
✅ **User Authentication** (JWT-based login)
✅ **Real-Time Code Collaboration** (WebSockets for live editing)
✅ **AI-Assisted Debugging** (GPT-4 for code suggestions)
✅ **Database Support** (PostgreSQL by default, fallback to SQLite)
✅ **Docker & Docker Compose Support**

---

## 1. Installation & Setup

### Clone the Repository
```bash
git clone https://github.com/your-repo.git
cd project-root
```

### Create & Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 2. Configuration
Update **`.env` file** or set environment variables:

```env
DATABASE_URL=postgresql://user:password@db:5432/app_db
REDIS_URL=redis://redis:6379
SECRET_KEY=mysecretkey
OPENAI_API_KEY=your-openai-api-key
```

**To use SQLite instead of PostgreSQL,** set:
```env
DATABASE_URL=sqlite:///./test.db
```

---

## 3. Running the Application

### Option 1: Run Manually
```bash
uvicorn app.main:app --reload
```

### Option 2: Run with Docker
```bash
docker-compose up --build
```

---

## 4. API Usage

### Register a User
```bash
curl -X POST "http://localhost:8000/auth/register" -H "Content-Type: application/json" -d '{"username":"testuser", "email":"test@example.com", "password":"testpass"}'
```

### Login (Retrieve JWT Token)
```bash
curl -X POST "http://localhost:8000/auth/token" -H "Content-Type: application/x-www-form-urlencoded" -d "username=testuser&password=testpass"
```

### Use JWT Token to Create a Code File
```bash
curl -X POST "http://localhost:8000/code/" -H "Authorization: Bearer YOUR_JWT_TOKEN" -H "Content-Type: application/json" -d '{"filename": "test.py", "content": "print(\"Hello World\")"}'
```

### Start a WebSocket Editing Session (With JWT Token)
```bash
ws://localhost:8000/ws/{document_id}/{user_id}?token=YOUR_JWT_TOKEN
```

---

## 5. Running Tests
```bash
pytest tests/
```

