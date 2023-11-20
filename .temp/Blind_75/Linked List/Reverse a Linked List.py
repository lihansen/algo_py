# https://leetcode.cn/problems/reverse-linked-list/description/
# Problem: 206. Reverse Linked List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)
        p = head.next
        p.next = head
        head.next = None
        return new_head



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        pre = None
        curr = head

        while curr:
            temp = curr.next

            curr.next = pre
            pre = curr
            curr = temp

        return pre