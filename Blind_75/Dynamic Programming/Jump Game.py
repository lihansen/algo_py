# https://leetcode.cn/problems/jump-game/description/
# Problem: 55. Jump Game

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        rightmost = 0

        for i in range(len(nums)):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])

                if rightmost >= len(nums) - 1:
                    return True

        return False