from leetcode.leetcode import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for i in range(n)]

        for i in range(n):
            for j in range(i):
                if nums [i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        d = []
        for i in range(n):
            if not d or nums[i] > d[-1]:
                d.append(nums[i])
            else:
                left = 0
                right = len(d) - 1

                while left <= right:
                    mid = (left + right) >> 1
                    
                    if d[mid] < nums[i]:
                        left = mid + 1
                    else:
                        pos = mid
                        right  = mid - 1
                

                d[pos] = nums[i]
        return len(d)





sol = Solution()
sol1 = Solution1()
print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]))
print(sol.lengthOfLIS([0,1,0,3,2,3]))


print(sol1.lengthOfLIS([10,9,2,5,3,7,101,18]))
print(sol1.lengthOfLIS([0,1,0,3,2,3]))
