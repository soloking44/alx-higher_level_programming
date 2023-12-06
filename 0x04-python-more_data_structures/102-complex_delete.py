#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for p in list(a_dictionary.keys()):
        if a_dictionary[p] == value:
            a_dictionary.pop(p, None)
    return a_dictionary
