#!/usr/bin/python3
def uppercase(str):
    ustr = ''
    for char in str:
        if 'a' <= char <= 'z':
            ustr += chr(ord(char) - 32)
        else:
            ustr += char
    print(ustr)
