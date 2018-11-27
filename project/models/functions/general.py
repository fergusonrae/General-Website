#################
#### imports ####
#################

import nltk

###################
#### functions ####
###################


def check_if_similar(new_model, list_of_current_models):
    '''Takes a string and a list. Returns a list of string's highly related objects in the list'''
    possible_other_models = set()
    for model in list_of_current_models:
        if nltk.edit_distance(model, new_model) <= 2: # Check if the string is two or less letters away from an element of the list
            possible_other_models.add(model)
        for new_word in new_model.split(): # Check if any words in the string are in an element of the list
            if new_word in model.split():
                possible_other_models.add(model)
    return possible_other_models