#!/usr/bin/python3
def uppercase(str):
    for n in str:
        if ord(n) > 96 and ord(n) < 123:
            n = chr(ord(n) - 32)
        print("{:s}".format(n), end="")
    print()
