from leetcode import List
# partition equal subset sum 
# similar to knapsack 

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        n = len(nums)

        total = sum(nums)

        if total & 1 : # check whether this number is odd 
            return False 
        
        half = total // 2
        if max(nums) > half:
            return False
        
        
        dp = [[False] * (half + 1) for i in range(n)]

        for i in range(n): # not choose any item, remains a zero capacity
            dp[i][0] = True

        for i in range(1, n):
            for j in range(1, half + 1):
                if j >= nums[i] : # can choose i th num 
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i]] 

                else:
                    dp[i][j] = dp[i-1][j] # capacity is not enough,

        return dp[n-1][half]
    


sol = Solution()
print(sol.canPartition([1,2,3,6]))