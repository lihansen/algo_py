

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head or not head.next:
            return
            # find n

        n = 0
        p = head
        while p:
            n += 1
            p = p.next
        # print(n//2)
        d = {}
        p = head
        for i in range(n // 2):
            p = p.next

        for i in range(n // 2, -1, -1):
            if p:
                d[i] = p
                p = p.next
                d[i].next = None

        p = head
        for i in range(n // 2):
            if i in d:
                d[i].next = p.next
                p.next = d[i]
                p = d[i].next

        return head
