
from flask import Blueprint
from controllers.login import LoginController

blueprint = Blueprint('login', __name__)

blueprint.route('/register', methods=['GET', 'POST'])   (LoginController.register)
blueprint.route('/login',    methods=['GET', 'POST'])   (LoginController.login)
blueprint.route('/logout',   methods=['GET'])           (LoginController.logout)
