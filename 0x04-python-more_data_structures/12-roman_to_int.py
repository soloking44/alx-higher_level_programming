#!/usr/bin/python3
def roman_to_int(roman_string):
    val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    d = 0

    if type(roman_string) is str and roman_string:
        for q in range(len(roman_string) - 1, -1, -1):
            if val[roman_string[q]] >= d:
                result += val[roman_string[q]]
            else:
                result -= val[roman_string[q]]
            d = val[roman_string[q]]
    return result
