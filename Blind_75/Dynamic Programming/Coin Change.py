# https://leetcode.cn/problems/coin-change/description/
# Problem: 322. Coin Change

def coinChange(self, coins: list[int], amount: int) -> int:
    # stands for the min number of coins needs for the amount i

    dp = [float("inf") for i in range(amount + 1)]
    dp[0] = 0

    for i in range(amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1
