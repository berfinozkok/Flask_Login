from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////mnt/c/Users/berfn/OneDrive/Masaüstü/Flask_Login/login.db'
app.config['SECRET_KEY'] = 'secret-key-goes-here'

db = SQLAlchemy(app)
login_manager=LoginManager()
login_manager.init_app(app)

class User(UserMixin, db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(30), unique=True)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    user=User.query.filter_by(username='Anthony').first()
    login_user(user)
    return 'You are now logged in!'

@app.route('/home')
@login_required
def home():
    return 'The current user is' + current_user.username

if __name__=='__main__':
    app.run(debug=True)