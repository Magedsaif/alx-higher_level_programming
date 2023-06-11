#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for les in matrix:
        for num in les:
            print("{:d}".format(num), end=" " if num != les[-1] else "")
        print()
