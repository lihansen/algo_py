# https://leetcode.cn/problems/contains-duplicate/


# do not need to check all the elements, faster on average.
def containsDuplicate(nums: list[int]) -> bool:
    s = set()
    for n in nums:
        if n in s:
            return True
        else:
            s.add(n)
    return False


def containsDuplicate2(nums: list[int]) -> bool:
    return not len(set(nums)) == len(nums)
