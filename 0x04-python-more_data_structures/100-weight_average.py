#!/usr/bin/python3
def weight_average(my_list=[]):
    numerator = 0
    denominator = 0
    if my_list:
        for p in range(len(my_list)):
            numerator += my_list[p][0] * my_list[p][1]
            denominator += my_list[p][1]
        average = numerator / denominator
        return average
    else:
        return 0
