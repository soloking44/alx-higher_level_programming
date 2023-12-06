#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for p in range(len(new_list)):
        if new_list[p] == search:
            new_list[p] = replace
    return new_list
