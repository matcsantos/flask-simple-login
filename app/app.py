
from flask import Flask
from routes import router

def create_app():
    
    app = Flask(__name__)
    
    for blueprint in router.blueprints:
        app.register_blueprint(blueprint)

    return app
