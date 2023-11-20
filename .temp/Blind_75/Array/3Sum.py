# https://leetcode.cn/problems/3sum/

# sorting + two pointers

def threeSum(self, nums: list[int]) -> list[list[int]]:
    n = len(nums)
    nums.sort()
    res = list()

    for i in range(n-2):
        # skip duplicate for the first element
        if i > 0 and nums[i] == nums[i-1]:
            continue

        l = i + 1
        r = n - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1 # it ok to have the same a,b,c, the next iteration will still not satisfy the condition.
            elif s > 0:
                r -= 1
            elif s == 0:
                res.append([nums[i], nums[l], nums[r]])

                # skip duplicate, because we need to have the different a,b,c results.
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                # skip duplicate for the third element
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1
    return res


