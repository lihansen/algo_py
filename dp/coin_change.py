# k coins: c1, c2, ... , ck
# amount

# return the fewest num of coins that u need to make up that amount.

from functools import lru_cache
import time

coins = [2, 5, 1]
amount = 11

mem = [float("inf") for i in range(amount + 1)]


# simple recursion
def coin_change(coins, amount):
    if amount < 0:
        return -1
    if amount == 0:
        return 0

    res = float("inf")
    for coin in coins:
        sub_prob = coin_change(coins, amount - coin)
        if sub_prob != -1:
            res = min(res, sub_prob + 1)

    return -1 if res == float("inf") else res


# recursion with lru_cache
# unhashable type list for (list, num), so
def coin_change_lru(coins, amount):
    @lru_cache(maxsize=amount)
    def dp(m):
        if m < 0:
            return -1
        if m == 0:
            return 0
        res = float("inf")
        for coin in coins:
            sub_prob = dp(m - coin)
            if sub_prob != -1:
                res = min(res, sub_prob + 1)

        return -1 if res == float("inf") else res

    return dp(amount)


# memoization with self defined mem
def coin_change_mem(coins, amount):
    if amount < 0:
        return -1
    if amount == 0:
        mem[amount] = 0

    if mem[amount] == float('inf'):
        res = float("inf")
        for coin in coins:
            sub_prob = coin_change_mem(coins, amount - coin)
            if sub_prob != -1:
                res = min(res, sub_prob + 1)

        mem[amount] = -1 if res == float("inf") else res

    return mem[amount]


# bottom up dp
def coin_change_dp(coins, amount):
    dp = [float("inf") for i in range(amount + 1)]

    dp[0] = 0

    for i in range(len(dp)):
        for coin in coins:
            if i - coin >= 0: # this is important , make sure the index is in range
                dp[i] = min(dp[i], dp[i - coin] + 1)
    print(dp)
    return dp[amount] if dp[amount] != float("inf") else -1


if __name__ == "__main__":
    start_time = time.time()
    res = coin_change(coins, amount)
    end_time = time.time()
    execution_time = end_time - start_time
    print(res)
    print("{:.8e}".format(execution_time))
    print()

    # ground truth for each cases
    test = [coin_change(coins, i) for i in range(amount + 1)]
    print(test)

    start_time = time.time()
    res = coin_change_lru(coins, amount)
    end_time = time.time()
    execution_time = end_time - start_time
    print(res)
    print("{:.8e}".format(execution_time))
    print()

    start_time = time.time()
    res = coin_change_mem(coins, amount)
    end_time = time.time()
    execution_time = end_time - start_time
    print(res)
    print(mem)
    print("{:.8e}".format(execution_time))
    print()

    start_time = time.time()
    res = coin_change_dp(coins, amount)
    end_time = time.time()
    execution_time = end_time - start_time
    print(res)
    print("{:.8e}".format(execution_time))
    print()
