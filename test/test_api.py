from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register():
    response = client.post("/auth/register", json={"username": "testuser", "email": "test@example.com", "password": "testpass"})
    assert response.status_code == 200

def test_login():
    response = client.post("/auth/login", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_create_code_file():
    response = client.post("/code/", json={"filename": "test.py", "content": "print('Hello World')"})
    assert response.status_code == 200
    assert response.json()["filename"] == "test.py"
