# Reverse a linked list from position m to n. Do it in one-pass.

# Note: 1 ≤ m ≤ n ≤ length of list.

# Example:

# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL

from dataclasses import dataclass
@dataclass
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
@dataclass
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int):
        # for exception
        if not head or m == n:
            return head

        root = start = ListNode(None)
        root.next = head

        # set 'start' and 'end'
        for _ in range(m-1):
            start = start.next

        end = start.next

        for _ in range(n - m):
            tmp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = tmp

        return root.next
