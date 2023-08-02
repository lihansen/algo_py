# https://leetcode.cn/problems/climbing-stairs/description/

# leetcode climb stairs

def climbStairs(n: int) -> int:
    if n < 3:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]

    return dp[n]