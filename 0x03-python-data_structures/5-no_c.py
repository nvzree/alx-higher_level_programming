#!/usr/bin/python3
def no_c(my_string):
    '''removes all characters c and C from a string.'''
    result = ''
    for i in my_string:
        if i != 'c' and i != 'C':
            result += i
    return result
