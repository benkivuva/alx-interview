#!/usr/bin/python3

"""
This script defines a function, minOperations, to calculate the fewest number
of operations needed to result in exactly the desired number of 'H' characters
in a file.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly
    the desired number of 'H' characters.

    Args:
    - n (int): The desired number of 'H' characters in the file.

    Returns:
    - int: The fewest number of operations needed.

    If n is impossible to achieve, return 0.
    """
    min_operations, divisor = 0, 2

    while isinstance(n, int) and n > 1:
        while n % divisor:
            divisor += 1
        min_operations += divisor
        n = int(n / divisor)

    return min_operations
