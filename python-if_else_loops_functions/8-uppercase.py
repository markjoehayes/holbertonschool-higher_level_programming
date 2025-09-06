#!/usr/bin/python3
def uppercase(str):
    ustr = ""
    for c in str:
        c = ord(c)
        if (c >= 97 and c <= 122):
            c -= 32
        ustr += chr(c)
    print(ustr)
