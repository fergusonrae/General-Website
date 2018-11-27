#################
#### Imports ####
#################

import json
from flask import flash

# Database related imports
import boto3 #s3 bucket, should be setup locally

######################
#### S3 Functions ####
######################

def save_to_s3(bucket, file_name, data):
    '''Write data to s3 bucket without having to first save it locally'''
    s3 = boto3.resource('s3')
    file_extension = file_name.split('.')[-1]
    if file_extension == 'json':
        s3.Object(bucket, file_name).put(Body=(bytes(json.dumps(data, indent=2).encode('UTF-8'))))
    elif file_extension in ['xlsx', 'xls', 'csv']:
        s3.Object(bucket, file_name).put(Body=data)
    else:
        flash("File type of "+file_extension+" not supported for download.")

def create_bucket(bucket_name, location='us-east-2'):
    s3 = boto3.client('s3')
    print('attempting')
    s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': location})
    print('created')