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

def get_from_s3(bucket, file_name):
    '''Pulling data from s3 bucket, reading outside of what is returned may need knowledge about the type of file'''
    s3 = boto3.client('s3')
    content_object = s3.get_object(Bucket=bucket, Key=file_name)
    return content_object['Body'].read()

def list_files_and_folders(bucket, path=""):
    '''List all files in the bucket, optionally with the path passed in'''
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket)
    bucket = bucket.objects.filter(Prefix=path)
    keys = []
    for obj in bucket.all():
        keys.append("/".join(obj.key.split('/')[1:]))
    return keys

def list_only_folders(bucket, path=""):
    client = boto3.client('s3')
    result = client.list_objects(Bucket=bucket, Prefix=path, Delimiter='/')
    folders = [o.get('Prefix').replace(path, "").strip('/') for o in result.get('CommonPrefixes')]
    return folders

def list_buckets():
    '''Gets the raw bucket names from the AWS account'''
    s3 = boto3.resource('s3')
    return [bucket.name for bucket in s3.buckets.all()]
