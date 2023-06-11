#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a, b = len(tuple_a), len(tuple_b)
    if (a == 0):
        tuple_a = (0, 0)
    elif a < 2:
        tuple_a += 0,
    if (b == 0):
        tuple_b = (0, 0)
    elif b < 2:
        tuple_b += 0,
    return(tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
