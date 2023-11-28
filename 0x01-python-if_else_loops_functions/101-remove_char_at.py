#!/usr/bin/python3
def remove_char_at(str, n):
    newStr = ""
    for k in range(len(str)):
        if k == n:
            continue
        else:
            newStr += str[k]
    return newStr
