#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed = 0 
    try:
        p_list = my_list[:x]
        for item in p_list:
            printed += 1
            print("{:d}".format(x) end="")
        print()
    except Exception as e:
        print(f"\nAn Error occured: {e}")
    finally:
        return printed
    
