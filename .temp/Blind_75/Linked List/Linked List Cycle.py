#https://leetcode.cn/problems/linked-list-cycle/description/

# Problem: 141. Linked List Cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next:
            return False

        slow = head

        # fast = head.next
        # while slow != fast:
        #     if not fast or not fast.next:
        #         # reach the end of the list

        #         return False
        #     else:
        #         slow = slow.next

        #         fast = fast.next.next
        # return True

        fast = head
        while True:
            if not fast or not fast.next:
                return False

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        # return True



