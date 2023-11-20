# https://leetcode.cn/problems/longest-increasing-subsequence/description/
# Problem: 300. Longest Increasing Subsequence


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [1 for i in range(len(nums))]

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        print(dp)
        return max(dp)