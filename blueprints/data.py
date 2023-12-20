from flask import Blueprint, render_template, request, render_template_string, session, redirect;
from models.post_model import Post;
from database.database import db;
from models.follow_model import Follow
from sqlalchemy import desc;

data = Blueprint('data', __name__);

@data.route('/')
def getPosts():
    if(request.method == "GET"):

        follows = Follow.query.filter(Follow.user_id == session['user_id'])
        validArr = [Follow.followed.id for Follow in follows]
        validArr.append(session['user_id'])

        posts = Post.query.filter(Post.user_id.in_(validArr)).order_by(desc(Post.id))
    

        return render_template(
            'base.html',
            header_file='header.html',
            page_body='posts.html',
            posts=posts,
            follows=follows,
            session=session
        )
@data.route('/post', methods=['GET', 'POST'])
def makePost():
    if(session['user_id'] and request.method == 'POST'):
        post = Post(content=request.form['content'], user_id=session['user_id'])
        db.session.add(post)
        db.session.commit()
        return redirect('/data/')
    else:
        return 'ok!'
