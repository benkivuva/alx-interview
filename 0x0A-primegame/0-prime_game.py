#!/usr/bin/python3
""" Prime Game """


def is_prime(num):
    """ Check if a number is prime """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """ Determine the winner of the prime game """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Count the number of primes up to n
        primes_count = sum(1 for i in range(2, n + 1) if is_prime(i))

        # Determine the winner based on the number of primes
        if primes_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the player with the most wins
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
