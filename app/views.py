from flask import render_template, url_for
from forms import RegistrationForm, LoginForm
from app import app

app.config['SECRET_KEY'] = 'BREAD'

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

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)    

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)    
