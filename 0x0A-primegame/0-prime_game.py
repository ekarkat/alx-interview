#!/usr/bin/python3
""" Prime Game """


def is_prime(n):
    """Check if n is a prime number."""
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def next_prime(x):
    """Return the next prime number after x."""
    if x == 2:
        return 3

    candidate = x + 2
    while True:
        if is_prime(candidate):
            return candidate
        candidate += 1


def del_mult(n, lis):
    """Remove multiples of n from the list nums in place."""
    i = 0
    while i < len(lis):
        if lis[i] % n == 0:
            del lis[i]
        else:
            i += 1


def number_list(n):
    """Create a list of numbers from 1 to n."""
    return list(range(1, n + 1))


def isWinner(x, nums):
    """Determine the winner after x rounds given nums as the list of rounds."""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        numbers = number_list(n)
        turn = 0  # 0 for Maria, 1 for Ben
        prime = 2

        while True:
            if not any(is_prime(num) for num in numbers):
                if turn == 0:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            if turn == 0:  # Maria's turn
                del_mult(prime, numbers)
                prime = next_prime(prime)
                turn = 1  # Switch to Ben's turn
            else:  # Ben's turn
                del_mult(prime, numbers)
                prime = next_prime(prime)
                turn = 0  # Switch to Maria's turn

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
