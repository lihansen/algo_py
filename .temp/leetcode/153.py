from leetcode.leetcode import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right :
            mid = (left + right) // 2

            if nums[mid] < mid[right]:
                right = mid
            else:
                left = mid + 1

        return nums[left]
    
