# https://leetcode.cn/problems/house-robber/description/
# Problem: 198. House Robber
def rob(self, nums: list[int]) -> int:
    dp = [0 for i in range(len(nums))]

    dp[0] = nums[0]
    if len(nums) <= 1:
        return dp[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

    return dp[len(nums) - 1]


def rob(self, nums: list[int]) -> int:

    n = len(nums)

    if not n:
        return 0

    if n == 1:
        return nums[0]

    first = nums[0]
    second = max(nums[0], nums[1])

    for i in range(2, n):
        temp = second
        second = max(first + nums[i], second)
        first = temp

    return second