
from flask_socketio import SocketIO, join_room
from websocket.messages_namespace import MessageNamespace;
from websocket.status_namespace import StatusNamepace;

websocket = SocketIO()
websocket.on_namespace(MessageNamespace('/chat'))
websocket.on_namespace(StatusNamepace('/status'))


