#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for p in set(my_list):
        sum += p
    return sum
