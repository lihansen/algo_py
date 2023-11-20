# https://leetcode.cn/problems/top-k-frequent-elements/description/
#

# Problem: 347. Top K Frequent Elements

import heapq
from collections import Counter


# class Num:
#     def __init__(self, freq, val):
#         self.freq = freq
#         self.val = val

#     def __lt__(self, other):
#         return self.freq < other.freq
# [1,2,3,4,5] 2


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        heap = list()  # min heap, size k, heap top is the minimum kth largest
        i = 0
        for key, val in counter.items():
            if i < k:
                heapq.heappush(heap, (val, key))
            else:
                num = (val, key)

                if heap[0][0] < num[0]:
                    heapq.heappush(heap, num)
                    heapq.heappop(heap)

            i += 1

        return [num[1] for num in heap]

