#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    '''returns a new dictionary with all values multiplied by 2'''
    multiplied_dict = {}

    for k, v in a_dictionary.items():
        multiplied_dict[k] = v * 2
    return (multiplied_dict)
