#!/usr/bin/python3

def search_replace(my_list, search, replace):
    '''replaces all occurrences of an element by another in a new list.'''
    new = my_list.copy()
    for i, value in enumerate(new):
        if value == search:
            new[i] = replace
            continue
    return (new)
