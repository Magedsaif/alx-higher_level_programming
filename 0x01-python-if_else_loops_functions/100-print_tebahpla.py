#!/usr/bin/python3
for char in range(122, 96, -1):
    if(char % 2 != 0):
        char = char - 32
    print("{:s}".format(chr(char)), end="")
