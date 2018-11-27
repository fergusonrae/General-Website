#################
#### Imports ####
#################

from project.utility.functions import file_storage
from project.models.functions import name_conversion
from project.models.constants import model_attributes

###################
#### functions ####
###################

def add_model(model):
    bucket_name = name_conversion.convert(model, model_attributes.BUCKET)
    file_storage.create_bucket(bucket_name, location='us-east-2')

def store_report(model, report_file_name, data):
    file_path = client_attributes.REPORTS_FOLDER + report_file_name
    file_storage.save_to_s3(model, file_path, data)