from flask import Blueprint, session, render_template, request, redirect;
from models.user_model import User;
from models.follow_model import Follow;
from database.database import db;

follow = Blueprint('follow', __name__);

# @follow.route('/follow_user')
@follow.route('/show_followers', methods=['GET', 'POST'])
def show_followers():
    users = [];
    if 'username' in request.form:
        followers = Follow.query.filter(Follow.user_id == session['user_id']).all();
        followedArr = [follower.followed.id for follower in followers]
        users = User.query.filter(User.id != session['user_id'], User.username == request.form['username'], ~User.id.in_(followedArr)).all()
    return render_template('base.html', header_file='header.html', users=users, page_body='follow_users.html')

@follow.route('/add_follow<id>', methods=['GET', 'POST'])
def add_follow(id):
    if 'user_id' not in session:
        return redirect('/')
    follow = Follow(user_id=session['user_id'], followed_id=id)
    db.session.add(follow);
    db.session.commit();
    return redirect('/data/')