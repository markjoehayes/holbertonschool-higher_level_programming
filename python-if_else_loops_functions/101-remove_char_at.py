#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    for i in str:
        new_str.append(str[:n])
        new_str.append(str[n+1:])
    return new_str
