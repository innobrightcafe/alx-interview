#!/usr/bin/python3
"""
fuction to test minimum operations of the operands
"""
def minOperations(n):
    if n == 1:
        return 0
    
    operations = 0
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    
    return operations
