from flask import render_template, url_for
from app import app

app.config

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

