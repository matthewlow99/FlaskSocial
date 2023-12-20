from database.database import db;

class Follow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    followed_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship("User", foreign_keys=[user_id], backref=db.backref('followers', lazy=True), primaryjoin="Follow.user_id == User.id")
    followed = db.relationship("User", foreign_keys=[followed_id], backref=db.backref('following', lazy=True), primaryjoin="Follow.followed_id == User.id")

    def __repr__(self):
        return f"<Follow {self.id}>"


    
