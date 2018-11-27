#################
#### imports ####
#################

from project.models.functions import file_retrieval
from project.models.constants import model_attributes

###################
#### functions ####
###################

def convert(string, conversion):
    '''Takes a string representation of a model and returns the desired conversion'''
    if conversion == model_attributes.BUCKET:
        return string.replace('-', ' ').lower().replace(' ', '-') + model_attributes.MODEL_BUCKET_ENDING
    if conversion == model_attributes.NAME:
        return string.split( model_attributes.MODEL_BUCKET_ENDING)[0].replace('-', ' ').title()
    if conversion == model_attributes.URL_PATH:
        return string.split( model_attributes.MODEL_BUCKET_ENDING)[0].replace('-', ' ').lower().replace(' ', '-')
    #TODO: write out error handling for conversion type is not correct

def get_model_name(string):
    return convert(string, model_attributes.NAME)

def get_client_bucket(string):
    return convert(string, model_attributes.BUCKET)

def get_model_url_path(string):
    return convert(string, model_attributes.URL_PATH)

def create_model_name_mapping(models=[]): #TODO: should be changed into a stored table that is read from. 
    #If client cannot be found in table, it is added.
    if not models:
        models = file_retrieval.list_models()
    models_list = []
    for model in models:
        model_dict = {}
        model_dict['name'] = model
        model_dict['url'] = convert(model, model_attributes.URL_PATH)
        model_dict['bucket'] = convert(model, model_attributes.BUCKET)
        model_list.append(model_dict)
    return model_list