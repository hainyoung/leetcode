# Reverse a singly linked list.

# Example:

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL

# explanation
# 연결 리스트를 뒤집는 문제는 매우 일반적이면서도 활용도가 높은 문제
# 재귀 recursive 구조와 반복 iterative 구조, 2가지 방식으로 풀이

# 1. recursive
from dataclasses import dataclass
@dataclass
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList1(self, head: ListNode):
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev

            next, node.next = node.next, prev
            return reverse(next, node)
        
        return reverse(head)
