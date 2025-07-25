#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'C': 100, 'D': 500, 'M': 1000}

    result = 0
    i = 0

    while i < len(roman_string):
        if i + 1 < len(roman_string) and roman_map[roman_string[i] 
            < roman_map[roman_string[i +1]]]:
            result += roman_map[roman_string[i +1]] - roman_map[roman_string[i]]
        else:
            result += roman_map[iroman_string[i]]
        i += 1
        return result

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

