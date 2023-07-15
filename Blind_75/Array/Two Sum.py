# https://leetcode.cn/problems/two-sum/

def twoSum(nums: list[int], target: int) -> list[int]:

    d = dict()
    n = len(nums)

    for i in range(n):
        r = target - nums[i]
        if r in d:
            return [d[r], i]
        else:
            d[nums[i]] = i

    return []



res = twoSum([2,7,11,15], 9)
print(res)