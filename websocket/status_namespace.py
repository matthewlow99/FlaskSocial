from flask import session;
from models.user_model import User;
from flask_socketio import Namespace, join_room, close_room;
from models.follow_model import Follow;
from database.database import db;

class StatusNamepace(Namespace):


    def on_connect(self):
        
        join_room(session.get('user_id'));
        user = User.query.filter(User.id == session.get('user_id')).first()

        if user:
            user.online = 1;
            db.session.commit();            

        followers = Follow.query.filter(Follow.user_id == session.get('user_id')).all();
        arr = [{'id': follow.followed_id, 'name': follow.followed.username } for follow in followers];
        
        for follow in arr:
            self.emit('status', {'id': session.get('user_id'), 'online': 1}, room=follow.get('id'))


    

    def on_disconnect(self):
        print('status disconnected')
        user = User.query.filter(User.id == session.get('user_id')).first()
        if user:
            user.online = 0;
            db.session.commit()

        followers = Follow.query.filter(Follow.user_id == session.get('user_id')).all();
        arr = [{'id': follow.followed_id, 'name': follow.followed.username } for follow in followers];
        for follow in arr:
            self.emit('disconnect', {'id': session.get('user_id'), 'online': 0}, room=follow.get('id'))
    
