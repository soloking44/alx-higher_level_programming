#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {p: a_dictionary[p] * 2 for p in a_dictionary}
    return new_dict
