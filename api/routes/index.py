from flask import Blueprint
from blinker import *
blueprint = Blueprint('blueprint', __name__)
from controllers.UserController import AllUsers,CreateNewUser

# User Routes 

# GET - Get All Users 
blueprint.route('/',methods=['GET'])(AllUsers)

# GET - Get All Users 
blueprint.route('/create',methods=['POST'])(CreateNewUser)