#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best_score = list(a_dictionary.keys())[0]
        for p in a_dictionary.keys():
            if a_dictionary[p] > a_dictionary.get(best_score):
                best_score = p
        return best_score
