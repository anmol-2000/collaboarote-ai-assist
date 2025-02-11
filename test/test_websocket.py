import pytest
from fastapi.testclient import TestClient
from starlette.websockets import WebSocketDisconnect
from app.main import app

client = TestClient(app)

@pytest.fixture
def websocket_client():
    with client.websocket_connect("/ws/testdoc/testuser") as ws:
        yield ws

def test_websocket_connection(websocket_client):
    websocket_client.send_text("Hello from test user")
    message = websocket_client.receive_text()
    assert "testuser: Hello from test user" in message
