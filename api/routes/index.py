from flask import Blueprint
from blinker import *
blueprint = Blueprint('blueprint', __name__)
from controllers.UserController import AllUsers,GetUser

# User Routes 

# GET - Get All Users 
blueprint.route('/',methods=['GET'])(AllUsers)


# GET - Get User 
blueprint.route('/<userid>',methods=['GET'])(GetUser)




