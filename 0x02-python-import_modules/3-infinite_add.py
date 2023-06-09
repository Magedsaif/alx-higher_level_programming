#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv as av
    ac = len(av) - 1
    i = 1
    a = 0
    while i <= ac:
        a = a + int(av[i])
        i = i + 1
    print("{:d}".format(a))
