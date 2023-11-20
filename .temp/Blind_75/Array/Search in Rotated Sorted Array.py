#https://leetcode.cn/problems/search-in-rotated-sorted-array
# Problem: 33. Search in Rotated Sorted Array
def search(self, nums: list[int], target: int) -> int:
    n = len(nums)

    left, right = 0, n - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
            # left part is sorted
        elif nums[mid] >= nums[left]:
            if nums[left] <= target < nums[mid]:  # target in left part range
                right = mid - 1

            else:  # left not in this range,
                left = mid + 1

        else:  # right part is sorted
            if nums[mid] < target <= nums[right]:  # target is in the right sorted part range
                # drop the left part
                left = mid + 1
            else:  # target is in the left unsorted part
                # drop the sorted right part and find the next sorted part in the left part subarray

                right = mid - 1

    return -1


# def search(self, nums: list[int], target: int) -> int:
#     n = len(nums)
#     left = 0
#     right = n - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         if nums[mid] == target:
#             return mid
#
#         if nums[mid] >= nums[0]:  # [0, mid-1] in order
#             if nums[0] <= target < nums[mid]:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#
#
#         else:  # [mid+ 1, ] in order
#             if nums[mid] < target <= nums[n - 1]:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#
#     return -1
