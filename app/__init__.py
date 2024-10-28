# app/__init__.py
from flask import Flask
from .routes import main_bp
from .auth import setup_auth

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    # Register Blueprints
    app.register_blueprint(main_bp)
    
    # Set up admin authentication
    setup_auth(app)
    
    return app
