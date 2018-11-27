#################
#### imports ####
#################
 
from flask import render_template, Blueprint
 
 
################
#### config ####
################
 
home_blueprint = Blueprint('home', __name__, template_folder='templates')
 
 
################
#### routes ####
################
 
@home_blueprint.route('/')
def index():
    return render_template('homepage.html')