#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for i in range(len(my_list)):
        if search == my_list[i]:
            my_list[i] = replace
    return my_list
