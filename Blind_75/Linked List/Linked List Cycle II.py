# https://leetcode.cn/problems/linked-list-cycle-ii/description/
# Problem: 142. Linked List Cycle II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return

            slow = slow.next
            fast = fast.next.next
        # while True:
        #     if not fast or not fast.next:
        #         return

        #     slow = slow.next
        #     fast = fast.next.next

        #     if slow == fast:
        #         break

        # print(slow.val)
        fast = head
        slow = slow.next # slow needs to move one step forward, because the fast pointer starts from head.next
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return fast

# or

'''
two times of meeting point - 2 * a = a + b + c + b
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return

        slow = head
        fast = head

        while True:
            if not fast or not fast.next:
                return

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        fast = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return fast


