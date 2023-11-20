# https://leetcode.cn/problems/house-robber-ii/description/
# Problem: 213. House Robber II

class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        if n == 2:
            return max(nums[0], nums[1])

        return max(self.helper(nums, 0, n - 1), self.helper(nums, 1, n))

    def helper(self, nums, start, end):
        first = nums[start]

        second = max(nums[start + 1], nums[start])

        for i in range(start + 2, end):
            temp = second
            second = max(first + nums[i], second)
            first = temp
        return second
