from flask import Flask, render_template, request, redirect, session
from database.db_config import db_config
from database.database import db
from models.user_model import User
from blueprints.account import account_bp
from blueprints.data import data;
from blueprints.follow import follow;
from blueprints.messages import message_bp;
from flask_migrate import Migrate;
from websocket.socket_config import websocket;


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flasksocial.db'
app.config['SECRET_KEY'] = 'helloworld!!#'
db.init_app(app)
websocket.init_app(app)

app.register_blueprint(account_bp, url_prefix='/account')
app.register_blueprint(data, url_prefix='/data')
app.register_blueprint(follow, url_prefix='/follow')
app.register_blueprint(message_bp, url_prefix='/messages')

@app.route('/', methods=['GET', 'POST'])
def index():
    if(request.method == 'GET'):
        if 'user_id' in session:
            print(session['user_id'])
            return redirect('/data/')
        return render_template('base.html', page_body='home.html', header_file='header.html');

@app.route('/migrate')
def migrate():
    Migrate(app, db)
    return 'migration complete';

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print('Database created successfully')
    app.run(debug=True)
    websocket.run(app)