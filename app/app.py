
from flask import Flask
from routes import router
import database
import os

def create_app():
    
    app = Flask(__name__)
    
    for blueprint in router.blueprints:
        app.register_blueprint(blueprint)
    
    if not os.path.exists('database/database.db'):
        database.setup()

    return app
