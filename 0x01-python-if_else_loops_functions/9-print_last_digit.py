#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -1 * number
    last_number = number % 10
    print("{:d}".format(last_number), end="")
    return (last_number)
