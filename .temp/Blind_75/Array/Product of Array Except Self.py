# https://leetcode.cn/problems/product-of-array-except-self/description/
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# left right product table

# offset 1, each product exclude the current elem

def productExceptSelf(self, nums: list[int]) -> list[int]:

    left = [1]
    right = [1]

    for i in range(len(nums)-1):
        left.append(left[-1] * nums[i])

    for i in range(len(nums)-1, 0, -1):
        right.append(right[-1] * nums[i])

    right.reverse()

    return [left[i] * right[i] for i in range(len(nums))]