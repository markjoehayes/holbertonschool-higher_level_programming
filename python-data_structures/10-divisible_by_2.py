#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    output_list = []
    for i in my_list:
        if (i % 2 == 0):
            output_list.append(True)
        else:
            output_list.append(False)
    return output_list
