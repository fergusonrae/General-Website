
#############################
#### S3 Structure Checks ####
#############################

def is_single_file(path):
    '''Checks to see that the path contains only a single file and not a folder'''
    if path[:-1] != '/' and len(path.split('/')) == 1:
        return True
    return False

def has_folder(path):
    '''Checks that the path contains a folder or nested files'''
    if not is_single_file(path):
        return True
    return False

def is_empty_folder(path):
    '''Checks that the path consists of only an empty folder'''
    if path[:-1] == '/' and len(path.split('/')) == 1:
        return True
    return False