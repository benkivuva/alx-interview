#!/usr/bin/python3
"""
Prime Game Module: Defines function that determines the winner after a certain
number of rounds of playing the Prime Game.
"""


def is_prime(num):
    """ Check if a number is prime """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """
    Determines the winner after a certain number of rounds
    of playing the Prime Game
    The Prime Game is a list of consecutive ints starting from 1 up to and
    including n. Players take turns picking prime numbers, which removes
    that number and all multiples of that number from the set. The player that
    has no more prime numbers to choose loses the game.
    Maria and Ben are playing the game, and Maria always goes first.
    Given the number of rounds, n, determine who the winner is.
    parameters:
        x [int]:
            the number of rounds
        nums [list of ints]:
            list of all ns for each round
    returns:
        the name of the player that won the most rounds,
        if both players play optimally,
        or None, if the winner cannot be determined
    """
    if not nums or x < 1:  # if nums is empty or x is less than 1
        return None
    winner_count = {"Maria": 0, "Ben": 0}
    for n in nums:
        primes_count = sum(1 for i in range(2, n + 1) if is_prime(i))
        if primes_count % 2 == 0:
            winner_count["Ben"] += 1
        else:
            winner_count["Maria"] += 1

    if winner_count["Maria"] > winner_count["Ben"]:
        return "Maria"
    elif winner_count["Ben"] > winner_count["Maria"]:
        return "Ben"
    else:
        return None
