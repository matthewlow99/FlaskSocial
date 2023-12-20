from database.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    online=db.Column(db.Integer, default=0);
    
    def __repr__(self) -> str:
        return "User created"
