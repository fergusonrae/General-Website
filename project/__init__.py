#################
#### imports ####
#################
 
from flask import Flask
 
 
################
#### config ####
################
 
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')

####################
#### blueprints ####
####################
 
from project.home.views import home_blueprint
from project.models.views import models_blueprint
 
# register the blueprints
app.register_blueprint(home_blueprint)
app.register_blueprint(models_blueprint)