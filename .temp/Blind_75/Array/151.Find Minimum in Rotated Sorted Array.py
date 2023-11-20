# https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/

# left part is in increasing order and strictly greater than the right part

# to find the minimum,
# compare the mid with the right

# if mid < right, both mid and right are in the right part,
#       from mid to right is in ascending order, so we need to find it from left to mid

# if mid > right, mid is in the left part, and right is in the right part,
#       we need to find it from mid + 1 to right
#

def findMin(self, nums: list[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] < nums[right]: #
            right = mid
        else:
            left = mid + 1
    return nums[right]
