from datetime import datetime
from flask import render_template, url_for, flash, redirect
from flask_sqlachemy import SQLAlchemy
from app import app
from forms import RegistrationForm, LoginForm


app.config['SECRET_KEY'] = 'BREAD'
app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       title = db.Column(db.String(100), nullable=False)
       date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
       content = db.Column(db.Text, nullable=False)
       user_id = db.Column(db.Integer, db.ForeignKey('user_id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}')"



posts = [
    {
        'author': 'Ivy Mwende',
        'title' : 'Pitch post 1',
        'content': 'First pitch content',
        'date_posted': 'April 20, 2018'
    },

    {
        'author': 'John Doe',
        'title' : 'Pitch post 2',
        'content': 'Second pitch content',
        'date_posted': 'April 21, 2018'
    },
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title='Home')    

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)    

@app.route('/login')
def login():
    form = LoginForm()
    if form.email.data == 'admin@blog.com' and form.password.data == 'password':
        flash('Yo have been logged in!', 'success')
        return redirect(url_for('home'))
    else:
        flash('Login Unsuccessful .Please check username or password', 'danger')  
        return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)    

if __name__ == '__main__':
    app.run(debug = True)