#!/usr/bin/python3
""" Prime game function """


def is_prime(n):
    """ check if n is prime """
    for i in range(2, n):
        if n % i == 0:
            return False
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
    return list(range(1, n + 1))


def isWinner(x, nums):
    """ Return the winner """
    i = 0
    maria = {"turn": True, 'wins': 0}
    ben = {"turn": False, 'wins': 0}
    for turn in range(x):
        numbers = number_list(nums[i])
        prime = 2

        # print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        # print("round {} , numbers are {} ".format(turn, numbers))

        if numbers == [1]:
            ben['wins'] += 1
            # print('jack pot maria wins')
            i += 1
            maria['turn'] = True
            ben['turn'] = False
            continue

        while True:
            # print(numbers)
            if maria['turn']:
                # print("maria round")
                if len(numbers) == 1:
                    ben['wins'] += 1
                    maria['turn'] = True
                    ben['turn'] = False
                    i += 1
                    # print("maria wins : {}".format(maria['wins']))
                    # print("ben wins : {}".format(ben['wins']))
                    break
                del_mult(prime, numbers)
                prime = next_prime(prime)
                maria['turn'] = False
                ben['turn'] = True

            else:
                # print("ben round")

                if len(numbers) == 1:
                    maria['wins'] += 1
                    ben['turn'] = False
                    maria['turn'] = True
                    i += 1
                    # print("maria wins : {}".format(maria['wins']))
                    # print("ben wins : {}".format(ben['wins']))
                    break
                del_mult(prime, numbers)
                prime = next_prime(prime)
                ben['turn'] = False
                maria['turn'] = True

    if maria['wins'] > ben['wins']:
        return "Maria"
    if ben['wins'] > maria['wins']:
        return "Ben"
    if ben['wins'] == maria['wins']:
        return None
