# Reverse a singly linked list.

# Example:

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL


# 1. recursive
from dataclasses import dataclass
@dataclass
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList1(self, head: ListNode):
        def reverse(node: Listnode, prev: None):
            if not node:
                return prev
            
            next, node.next = node.next, prev
            return reverse(next, node)
        
        return reverse(head)


# 2. iterativ
def reverseList2(self, head: ListNode):
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev

