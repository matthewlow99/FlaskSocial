from flask import session;
from sqlalchemy import or_, and_;
from flask_socketio import SocketIO, join_room, close_room, Namespace, emit, send, disconnect;
from models.message_model import Message;
from database.database import db;


class MessageNamespace(Namespace):
    def on_connect(self):
        print('socket connected')
        join_room(session.get('user_id'))
    def on_disconnect(self):
        print('room closed')
        close_room(session.get('user_id'))
    def on_retrieve(self, data):

        print('this does work?')

        myID = session.get('user_id');
        otherID = data.get('to_id');

        messages = Message.query.filter(or_(
            and_(Message.from_id == myID, Message.to_id == otherID),
            and_(Message.from_id == otherID, Message.to_id == myID)
        )).all()

        message_arr = [{'message': message.message, 'from_user': message.from_user.username} for message in messages]
        self.emit('retrieve', message_arr, room=session.get('user_id'))

    def on_send(self, data):
        print(data)
        message = data.get('message')
        to_id = data.get('to_id');
        user_id = session.get('user_id')

        message = Message(message=message, from_id=user_id, to_id=to_id)
        db.session.add(message)
        db.session.commit()

        myID = user_id;
        otherID = to_id;

        messages = Message.query.filter(or_(
            and_(Message.from_id == myID, Message.to_id == otherID),
            and_(Message.from_id == otherID, Message.to_id == myID)
        )).all()

        message_arr = [{'message': message.message, 'from_user': message.from_user.username} for message in messages]
        self.emit('retrieve', message_arr, room=session.get('user_id'))
        self.emit('retrieve', message_arr, room=to_id)