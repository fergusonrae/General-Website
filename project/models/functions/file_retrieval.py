#################
#### Imports ####
#################

from flask import flash

# Application function imports
from project.utility.functions import file_retrieval, file_structure
from project.models.functions import name_conversion
from project.models.constants import model_attributes

###################
#### functions ####
###################

def list_models():
    '''Pull out models from all available buckets. Only takes buckets that end in model'''
    buckets = file_retrieval.list_buckets()
    return [name_conversion.convert(
        bucket, model_attributes.NAME) for bucket in buckets if bucket.endswith(model_attributes.MODEL_BUCKET_ENDING)]

def list_model_reports(model): # TODO: pull out reports string into constant or client object attribute
    model_bucket = name_conversion.convert(model, model_attributes.BUCKET)
    files_folders = file_retrieval.list_files_and_folders(model_bucket, model_attributes.REPORTS_FOLDER)
    return files_folders

def get_reports(model): #TODO: needs a lot of work. 
    all_files = list_client_reports(client)
    available_reports = []
    current_reports = {}
    for report in all_files:
        print(report)
        if file_structure.is_empty_folder(report):
            available_reports.append(report)
        elif file_structure.has_folder(report):
            report_aspects = report.split('/')
            if len(report_aspects) != 2:
                flash('Error in depth of folder structure')
            if report_aspects[0] in current_reports:
                current_reports[report_aspects[0]].append(report_aspects[1])
            else:
                current_reports[report_aspects[0]] = list(report_aspects[1])

    return {'available': available_reports, 'current': current_reports}
