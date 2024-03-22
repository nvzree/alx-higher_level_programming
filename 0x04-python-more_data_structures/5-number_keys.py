#!/usr/bin/python3

def number_keys(a_dictionary):
    '''returns the number of keys in a dictionary.'''
    count = []
    for k, v in a_dictionary.items():
        count.append(k)
    return (len(count))
