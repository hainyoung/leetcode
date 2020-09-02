# 24
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = haed.next
            head.next = self.swapParis(p.next)
            p.next = head
            return p
        return head