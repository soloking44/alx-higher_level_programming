#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dictionary = sorted(a_dictionary)
    for p in sorted_dictionary:
        print("{}: {}".format(p, a_dictionary[p]))
