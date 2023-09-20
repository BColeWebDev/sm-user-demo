from flask import Blueprint
blueprint = Blueprint('blueprint', __name__)
from controllers.UserController import AllUsers

# User Routes 

# GET - Get All Users 
blueprint.route('/',methods=['GET'])(AllUsers)