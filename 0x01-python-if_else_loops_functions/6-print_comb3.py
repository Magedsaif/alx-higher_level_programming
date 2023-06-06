#!/usr/bin/python3
for n in range(0, 9):
    for j in range(n + 1, 10):
        print("{}{}".format(n, j), end ="")
        if n == 8 and j == 9:
            print()
        else:
            print(", ", end="")
