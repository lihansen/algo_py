# https://leetcode.cn/problems/maximum-subarray/

# Given an integer array nums, find the subarray with the largest sum, and return its sum.


# without compression
def maxSubArray(nums) -> int:
    if not nums:
        return 0

    dp = [0 for i in range(len(nums))] # dp array stands for the max subarr ends with i th elem
    dp[0] = nums[0] # the first elem should be the first elem, for 1-length array

    for i in range(1, len(nums)):
        dp[i] = max(nums[i], nums[i] + dp[i - 1]) # update the elem from left to right traversing

    return max(dp)


# todo: comments
# compression
def maxSubArr_cmprs(nums):
    dp = nums[0]
    pre = 0

    for i in range(1, len(nums)):
        pre = max(nums[i], nums[i] + pre)
        dp = max(pre, dp)


    return dp


res = maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(res)

res = maxSubArr_cmprs([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(res)
