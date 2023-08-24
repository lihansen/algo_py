# https://leetcode.cn/problems/merge-intervals/description/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        n = len(intervals)
        del_start = 0
        for i in range(1, n):
            if intervals[ i -1][1] >= intervals[i][0]:
                intervals[i][0] = intervals[ i -1][0] # starts
                intervals[i][1] = max(intervals[i][1], intervals[ i -1][1])
                # drop the previous interval by swapping
                intervals[del_start], intervals[i - 1] = intervals[i - 1], intervals[del_start]
                del_start += 1


        return intervals[del_start:]
