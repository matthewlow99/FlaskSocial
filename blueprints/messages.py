from flask import Blueprint, render_template, redirect, session
from models.message_model import Message;
from models.follow_model import Follow
message_bp = Blueprint('message', __name__);

@message_bp.route('/all')
def index():
    following = Follow.query.filter(Follow.user_id == session['user_id']).all()
    return render_template('base.html', page_body='message_home.html', followers=following)

@message_bp.route('/<friend_id>')
def friend(friend_id):
    follower = Follow.query.filter(Follow.followed_id == friend_id).first()
    
    return render_template('base.html', page_body='message_view.html', session=session, friend=follower);

# @message_bp.route('/send_me')