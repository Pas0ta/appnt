import os
from flask import Flask

app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat_app.db'
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'a_very_secret_key')