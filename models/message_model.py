from database.database import db;
from datetime import datetime

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True);
    message = db.Column(db.String(255), nullable=False);
    from_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False); 
    to_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False);
    to_user = db.relationship('User', backref=db.backref('from_messages', lazy=True), foreign_keys=[to_id], primaryjoin=("Message.to_id == User.id"))
    from_user = db.relationship('User', backref=db.backref('to_messages', lazy=True), foreign_keys=[from_id], primaryjoin=("Message.from_id == User.id"))
    timestamp = db.Column(db.String(255), default=datetime.utcnow());

    def __repr__(self):
        return '<Message %r>' % (self.message);
    
