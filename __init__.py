from flask import flask

app = Flask(__name__)

app.config.from_object("config.DevelopmentConfig")

from app import views

