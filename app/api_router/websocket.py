from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.utils.realtime import add_connection, remove_connection, broadcast

router = APIRouter()

@router.websocket("/{document_id}/{user_id}")
async def websocket_endpoint(websocket: WebSocket, document_id: str, user_id: str):
    await websocket.accept()
    add_connection(document_id, websocket)

    try:
        while True:
            data = await websocket.receive_text()
            await broadcast(document_id, f"{user_id}: {data}")
    except WebSocketDisconnect:
        remove_connection(document_id, websocket)
