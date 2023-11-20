# https://leetcode.cn/problems/non-overlapping-intervals/description/
# Problem: 435. Non-overlapping Intervals
# GREEDY
# sort by end time
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        ans = 1
        intervals.sort(key=lambda x: x[1])

        right = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] >= right:
                ans += 1
                right = intervals[i][1]

        return len(intervals) - ans