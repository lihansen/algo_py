# https://leetcode.cn/problems/maximum-subarray/description/

# dp
def maxSubArray(self, nums: list[int]) -> int:
    dp = [ nums[0] for i in range(len(nums))]

    for i in range(1, len(nums)):
        dp[i] = max(nums[i], dp[i-1] + nums[i])

    return max(dp)


def maxSubArray(self, nums: list[int]) -> int:
    pre_max = 0
    res = nums[0]

    for num in nums:
        pre_max = max(pre_max + num, num)
        res = max(pre_max, res)

    return res