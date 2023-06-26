#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    printed_list = []
    for i in range(list_length):
        division = 0
        try:
            division = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError, ValueError):
            print("division by 0")
        except (TypeError):
            print("wrong type")
        except (IndexError):
            print("out of range")
        finally:
            printed_list.append(division)
    return printed_list
