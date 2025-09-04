#!/usr/bin/python3
for i in range(97, 123):
    if (i == 101):
        continue
    elif(i == 113):
        continue
    end_char = "\n" if i == 122 else ""
    print("{}".format(chr(i)), end=end_char)
