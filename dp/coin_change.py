
# k coins: c1, c2, ... , ck
# amount

# return the fewest num of coins that u need to make up that amount.


# simple recursion
def coin_change(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return -1

    res = float("inf")
    for coin in coins:
        res = min (res, 1 + coin_change(coins, n - coin))
    return res
