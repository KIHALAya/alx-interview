#!/usr/bin/python3
"""0-making_change.py
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed
    to meet a given amount total.

    Args:
    coins (list): A list of integers representing
    the values of the coins in your possession.
    total (int): The total amount you want to achieve
    with the fewest number of coins.

    Returns:
    int: The fewest number of coins needed to meet the total.
    If the total is 0 or less, returns 0.
    If the total cannot be met
    by any combination of the coins you have, returns -1.
    """

    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # base case

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
