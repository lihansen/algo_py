# https://leetcode.cn/problems/longest-palindromic-subsequence/description/


# Problem: 516. Longest Palindromic Subsequence

# reverse the string and find the longest common subsequence


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        dp = [[0 for i in range(n)] for j in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1

            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]




class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.longest_common_str(s, s[::-1])

    def longest_common_str(self, s1, s2):
        m = len(s1) + 1
        n = len(s2) + 1

        dp = [[0 for i in range(n)] for j in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1

                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m - 1][n - 1]
