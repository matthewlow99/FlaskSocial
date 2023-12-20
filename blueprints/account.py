from flask import Blueprint, request, render_template, redirect, session;
from database.database import db
from models.user_model import User

account_bp = Blueprint('account_bp', __name__)

@account_bp.route('/create_account', methods=['GET', 'POST'])
def createAccount():
    if(request.method == 'GET'):
        return render_template('base.html', page_body='create_account.html', header_file='header.html');
    elif(request.method == 'POST'):
        username = request.form['username'];
        password = request.form['password'];
        password1 = request.form['password1'];

        if(password != password1):
            return 'Password must match'
        
        user = User(username=username, password = password);
        db.session.add(user);
        db.session.commit();
        return redirect('/')
    
@account_bp.route('/login', methods=['GET', 'POST'])
def login():
    if(request.method == 'POST'):
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username, password=password).one_or_none()
        
        if(user == None):
            return 'Invalid credentials';
        else:
            session['user_id'] = user.id;
            session['username'] = user.username;
            return redirect('/');
    return render_template('base.html', header_file='header.html', page_body='login.html')
@account_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/')

