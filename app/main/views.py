from datetime import datetime
from flask import render_template, url_for, flash, redirect
from flask_sqlachemy import SQLAlchemy
from app import app
from forms import RegistrationForm, LoginForm


app.config['SECRET_KEY'] = 'BREAD'
app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAchemy(app)



@run.shell
def make_shell_context():
    return dict(app = app,db = db, User = User)



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