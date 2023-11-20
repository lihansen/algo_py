# https://leetcode.cn/problems/maximum-product-subarray/
# Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

# dp

# Because each elem can be either positive or negative, we need to keep track of both the max and min product
#
def maxProduct(self, nums: list[int]) -> int:
    # if not nums:
    #     return None

    max_product = nums[0]
    min_product = nums[0]
    res = nums[0]

    for i in range(1, len(nums)):
        pre_max = max_product

        # max_product stands for the max product indexing from 0 to i - 1
        max_product = max(max_product * nums[i], min_product * nums[i], nums[i])
        # min_product stands for the min product indexing from 0 to i - 1
        min_product = min(min_product * nums[i], pre_max * nums[i], nums[i])

        res = max(res, max_product)

    return res