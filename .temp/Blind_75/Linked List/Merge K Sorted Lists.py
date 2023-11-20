

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

# monkey patching
def lt(a, b):
    return a.val < b.val


ListNode.__lt__ = lt


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = list()
        new_head = ListNode()
        p = new_head
        for l in lists:
            if l:
                heapq.heappush(h, l)

        while h:
            min_node = heapq.heappop(h)
            p.next = min_node
            p = p.next
            if min_node.next:
                heapq.heappush(h, min_node.next)

        return new_head.next




















