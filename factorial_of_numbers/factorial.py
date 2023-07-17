#!/usr/bin/python3
"""
function that returns the factorial of a number
"""
def my_func(n):
    if n == 1:
        return 1
    else:
        return n *my_func(n-1)

