import uuid
from flask import Flask, render_template
from .models import DB, User, Tweet

def create_app():
    "Create and configure an instance of the Flask application"

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABSE_URI'] = 'sqlite:///C:\\Users\\btros\\Lambda\\TwitOff\\twitoff\\app_db.sqlite'
    DB.init_app(app)
    
    @app.route('/')
    def index():
        return 'Index Page'

    @app.route('/hello')
    def hello():
        return render_template('base.html', title='hello')
    return app
        


