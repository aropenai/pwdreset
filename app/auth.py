# app/auth.py
from flask import request, Response

def setup_auth(app):
    @app.before_request
    def basic_authentication():
        auth = request.authorization
        if not auth or not (auth.username == app.config['ADMIN_USER'] and auth.password == app.config['ADMIN_PASSWORD']):
            return Response('Access Denied', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})
