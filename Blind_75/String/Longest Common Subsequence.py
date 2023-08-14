# https://leetcode.cn/problems/longest-common-subsequence/description/description
# Problem: 1143. Longest Common Subsequence


# create a 2D table for two strings
# dp[i][j] represents the longest common subsequence of text1[:i] and text2[:j]
# dp[0][0] = 0

# similar to edit distance

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[j - 1] == text2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n][m]