# https://leetcode.cn/problems/decode-ways/description/
# Problem: 91. Decode Ways


def numDecodings(s: str) -> int:
    dp = [0 for i in range(len(s) + 1)]
    dp[0] = 1 # empty string has 1 way to decode

    for i in range(1, len(s) + 1): # indexing from 1, but s[i-1] is the ith char
        if s[i - 1] != '0':
            dp[i] += dp[i - 1] # the first char comes from dp[0] = 1

        #if i >= 2 and s[i - 2] != '0' and if int(s[i - 2: i]) <= 26:
        if i >= 2 and 10 <= int(s[i - 2: i]) <= 26: # 10 <= int(s[i - 2: i]) <= 26
            dp[i] += dp[i - 2]
    # print(dp)
    return dp[len(s)]



numDecodings("226")

# 2, 26
# 22, 6
# 2, 2, 6
