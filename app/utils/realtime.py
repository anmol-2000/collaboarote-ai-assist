from fastapi import WebSocket

connections = {}

def add_connection(document_id: str, websocket: WebSocket):
    if document_id not in connections:
        connections[document_id] = []
    connections[document_id].append(websocket)

def remove_connection(document_id: str, websocket: WebSocket):
    connections[document_id].remove(websocket)
    if not connections[document_id]:
        del connections[document_id]

def broadcast(document_id: str, message: str):
    for connection in connections.get(document_id, []):
        connection.send_text(message)
