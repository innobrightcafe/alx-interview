#!/usr/bin/python3
"""
function to test for the minimum number of operations
"""

def minOperations(n):
    """
    Fuction that gets fewest # of operations needed to result in exactly n H characters
    """
    # all outputs should be at least 2 char: (min, Copy All => Paste)
    if (n < 2):
        return 0
    opts, start = 0, 2
    while start <= n:
        # if n evenly divides by start
        if n % start == 0:
            # total even-divisions by start = total operations
            opts += start
            # set n to the remainder
            n = n / start
            # reduce start to find remaining smaller vals that evenly-divide n
            start -= 1
        # increment start until it evenly-divides n
        start += 1
    return opts
 