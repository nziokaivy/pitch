from flask import Flask
from flask_sqlachemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'BREAD'
app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAchemy(app)




from app import views