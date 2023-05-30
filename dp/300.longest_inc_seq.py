#Given an integer array nums, return the length of the longest strictly increasing subsequence.

# mathematical induction

def longest_inc_subseq(nums):

    if not nums:
        return 0

    dp = [1 for i in range(len(nums))] # max len inc subseq ends with i th elem

    for i in range(len(nums)):
        for j in range(i):  # from 0 to i-1
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


res = longest_inc_subseq([10,9,2,5,3,7,101,18])
print(res)
