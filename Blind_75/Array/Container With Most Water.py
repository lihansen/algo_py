# https://leetcode.cn/problems/container-with-most-water/

# two pointers
def maxArea(height: list[int]) -> int:
    n = len(height)

    l = 0
    r = n - 1

    max_area = 0

    while l < r:
        min_h = min(height[l], height[r])
        length = r - l
        area = min_h * length
        max_area = max(area, max_area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_area





