# https://leetcode.cn/problems/find-median-from-data-stream/description/
# Problem: 295. Find Median from Data Stream


import heapq


class MedianFinder:

    def __init__(self):
        self.less = list()  # less than the median, max heap, negative, length is + 1
        self.greater = list()  # greater than the median, min heap

    def addNum(self, num: int) -> None:
        # max_heap [-1,-2,-3, -4], [5 ,6,7,8] min_heap

        if not self.less:  # no elems in less
            heapq.heappush(self.less, -num)
            return

        less_top = -self.less[0]
        if len(self.less) == len(self.greater):
            greater_top = self.greater[0]

            if num <= greater_top:
                heapq.heappush(self.less, -num)
            elif num > less_top:
                greater_top = heapq.heappop(self.greater)
                heapq.heappush(self.less, -greater_top)
                heapq.heappush(self.greater, num)

        elif len(self.less) == len(self.greater) + 1:  # more elems in less
            if num <= less_top:
                less_top == -heapq.heappop(self.less)
                heapq.heappush(self.greater, less_top)
                heapq.heappush(self.less, -num)
            elif num > less_top:
                heapq.heappush(self.greater, num)

    def findMedian(self) -> float:
        if not self.greater:
            return -self.less[0]

        if (len(self.less) + len(self.greater)) % 2 == 0:
            median = (self.greater[0] - self.less[0]) / 2

        else:
            median = -self.less[0]
        return median

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()