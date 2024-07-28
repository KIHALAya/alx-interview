#!/usr/bin/python3
def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
    coins (list): A list of integers representing the values of the coins in your possession.
    total (int): The total amount you want to achieve with the fewest number of coins.

    Returns:
    int: The fewest number of coins needed to meet the total. If the total is 0 or less, returns 0.
         If the total cannot be met by any combination of the coins you have, returns -1.
    """

    if total <= 0:
        return 0

    # Initialize dp array with a large number (total + 1) because total + 1 is impossible number of coins to form total.
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # base case

    # Build up the dp array
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still inf, return -1 as it means we cannot make the total with the given coins
    return dp[total] if dp[total] != float('inf') else -1
