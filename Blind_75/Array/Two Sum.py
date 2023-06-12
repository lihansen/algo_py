def twoSum(nums: list[int], target: int) -> list[int]:

    d = dict()

    for i in range(len(nums)):
        if target - nums[i] in d:
            return [d[target-nums[i]], i]
        else:
            d[nums[i]] = i

    return []



assert twoSum([2,7,11,15], 9) == [0, 1]