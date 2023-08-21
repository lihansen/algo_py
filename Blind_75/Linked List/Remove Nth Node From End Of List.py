

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        pre = ListNode()

        pre.next = head

        slow = pre
        fast = head

        for i in range(n):
            fast = fast.next

        while fast: # fast reaches the end
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return pre.next