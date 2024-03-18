#!/usr/bin/python3

def multiple_returns(sentence):
    ''' returns a tuple with the length of a string and its first character.'''

    length = len(sentence)
    if sentence == '':
        first = None
    else:
        first = sentence[0]

    return ((length, first))
