#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elements_printed = 0
    if(my_list):
        for i in range(x):
            try:
                print("{}".format(my_list[i]),end='')
                elements_printed = elements_printed + 1
            except IndexError:
                print()
                return(elements_printed)
    print()
    return(elements_printed)