# https://leetcode.cn/problems/insert-interval/
# Problem: 57. Insert Interval
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        n = len(intervals)

        # looking for overlaps
        del_begin = -1
        del_end = n - 1
        for i in range(n):
            if not (intervals[i][1] < newInterval[0] or newInterval[1] < intervals[i][0]):
                # have overlap
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(intervals[i][1], newInterval[1])
                if del_begin == -1:
                    del_begin = i
                del_end = i + 1

        # having overlaps, needs to delete some intervals
        if del_begin != -1:
            intervals = intervals[:del_begin] + intervals[del_end:]
        # no overlaps
        # intervals = intervals

        # looking for the insert position
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                return intervals[:i] + [newInterval] + intervals[i:]

        return intervals + [newInterval]

