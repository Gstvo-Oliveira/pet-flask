from flask import Flask
from .pet_routes import pet_routes

def init_app(app: Flask):
    pet_routes(app)
