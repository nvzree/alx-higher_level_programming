#!/usr/bin/python3
def element_at(my_list, idx):
    '''function that retrieves an element from a list'''
    for i in my_list:
        if idx < 0:
            return ('None')
        elif idx > (len(my_list) - 1):
            return ('None')
        elif idx == i:
            return (my_list[i])
