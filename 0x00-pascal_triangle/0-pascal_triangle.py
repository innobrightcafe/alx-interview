#!/usr/bin/python3
""" Module to generate Pascals triangle in an array """


def pascal_triangle(n):
    """
    function to find pascals triangle

        Args:
            n: integer numbers of rows to generate

        Return:
            base: pascal_triangle in an array
    """
    if n <= 0:
        return []

    base = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(base[i - 1][j - 1] + base[i - 1][j])
        row.append(1)
        base.append(row)

    return base
