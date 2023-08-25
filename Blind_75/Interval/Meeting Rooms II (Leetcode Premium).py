# https://leetcode.cn/problems/meeting-rooms-ii/description/
# Problem: 253. Meeting Rooms II


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        timestamp = []

        for interval in intervals:
            timestamp.append((interval[0], 1)) # start meeting, needs a room, +1
            timestamp.append((interval[1], -1)) # end meeting, releases a room, -1

        timestamp.sort() # eg: [start +1, end -1, start +1, end -1, ...]

        count = 0
        max_count = 0
        for t in timestamp:
            count += t[1]
            max_count = max(max_count, count)

        return max_count