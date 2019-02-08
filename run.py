from app import app
from app import create_app,db
from app.views import User

if __name__ == '__main__':
    app.run(debug = True)