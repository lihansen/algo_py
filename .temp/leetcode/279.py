class Solution1:
    
    # similar to coin change 
    def numSquares(self, n: int) -> int:


        coins = self.gen_coins(n)
        print(coins)
        dp = [float("inf") for i in range(n + 1)]
        dp[0] = 0
        

        for i in range(1, n + 1):
            for coin in coins :
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1) 
                
        return dp[n]

    def gen_coins (self, n):
        res = []

        coin = 1

        for i in range(1, n + 1):
            sq = i ** 2
            if sq > n:
                return res
            else:
                res.append(sq)


        return res

sol = Solution1()

print(sol.numSquares(1))