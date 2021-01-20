
from flask import Blueprint
from controllers.home import HomeController

blueprint = Blueprint('home', __name__)

blueprint.route('/') (HomeController.index)
