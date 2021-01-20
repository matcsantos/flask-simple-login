
from flask import Blueprint
from controllers.login import LoginController

blueprint = Blueprint('login', __name__)

blueprint.route('/register', methods=['GET', 'POST']) (LoginController.register)
