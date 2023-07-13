#!/usr/bin/python3
"""Pascal."""


def pascal_triangle(n):
    """Pascal."""

    if n <= 0:
        return []

    list_t = [[1], [1, 1]]
    for i in range(2, n):
        list_row = []
        list_row.append(1)
        list_row.append(1)
        for j in range(1, i):
            list_row.insert(j, list_t[i - 1][j] + list_t[i - 1][j - 1])
        list_t.append(list_row)
    return list_t[:n]
