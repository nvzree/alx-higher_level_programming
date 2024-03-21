#!/usr/bin/python3

def uniq_add(my_list=[]):
    '''adds all unique integers in a list (only once for each integer).'''
    uniq_list = list(set(my_list))
    add = 0
    for x in uniq_list:
        add += int(x)
    return add
