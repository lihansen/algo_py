

# https://leetcode.cn/problems/unique-paths/description/
# Problem: 62. Unique Paths


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1,m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        print(dp)
        return dp[m-1][n-1]
from functools import lru_cache
class Solution:
    @lru_cache()
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 or n==1:
            return 1
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        mem = [[0 for i in range(n)] for j in range(m)]

        return self.helper( m -1, n- 1, mem)

    def helper(self, m, n, mem):
        if m == 0 or n == 0:
            mem[m][n] = 1
            return 1

        elif mem[m][n] == 0:
            mem[m][n] = self.helper(m - 1, n, mem) + self.helper(m, n - 1, mem)

        return mem[m][n]