from database.database import db;

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True);
    content = db.Column(db.String(1000), nullable=False);
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('posts', lazy=True))
    
    def __repr__(self):
        return self;