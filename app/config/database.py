from flask import Flask
from flask_pymongo import PyMongo
import os

def init_app(app:Flask):
    app.config['MONGO_URI'] = os.getenv("DATABASE_URL")
    mongo = PyMongo(app)
    app.db = mongo.db
    return app