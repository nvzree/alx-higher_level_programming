#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    '''function that prints all integers of a list'''
    if my_list is not None:
        for i in my_list[::-1]:
            print('{:d}'.format(i))
