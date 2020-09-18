# Given a linked list, swap every two adjacent nodes and return its head.

# You may not modify the values in the list's nodes, only nodes itself may be changed.

 

# Example:

# Given 1->2->3->4, you should return the list as 2->1->4->3.

from dataclasses import dataclass

# 1. swap only values
# Definition for singly-linked list.
@dataclass
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

@dataclass
class Solution1:
    def swapPairs1(self, head: ListNode):
        cur = head

        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next

        return head

# 2. swap using repetitive structure

@dataclass
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

@dataclass
class Solution2:
    def swapPairs2(self, head: ListNode):
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head

            prev.next = b

            head = head.next
            prev = prev.next.next
        
        return root.next

# 3. swap using recursive structure
@dataclass
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
@dataclass
class Solution:
    def swapPairs3(self, head: ListNode):
        if head and head.next:
            p = head.next
            head.next = self.swapPairs3(p.next)
            p.next = head
            return p

        return head
