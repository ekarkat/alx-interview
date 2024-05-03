#!/usr/bin/python3
""" coins change challenge """


def makeChange(coins, total):
    """ Function description """
    coins.sort(reverse=True)
    number_of_coins = 0

    if not total:
        return 0
    print(coins)
    for coin in coins:
        num = total // coin
        total = total - (coin*num)
        number_of_coins += num
    if total == 0:
        return(number_of_coins)
    return -1
