#################
#### imports ####
#################
 
from flask import render_template, Blueprint
 
 
################
#### config ####
################
 
models_blueprint = Blueprint('models', __name__, template_folder='templates')
 
 
################
#### routes ####
################

@models_blueprint.route('/models')
def models_homepage():
    return render_template('models_homepage.html')

@models_blueprint.route('/models/beauty')
def beauty_classification():
    return render_template('beauty_classification.html')