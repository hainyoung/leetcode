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
# explanation
# 직관적인 방법 동시에 변칙적인 방법
# 연결리스트의 노드를 변경하는 게 아닌 노드 구조는 그대로 유지하되 값만 변경
# 실용성과는 거리가 먼 방법
# 대개 연결 리스트는 복잡한 여러 가지 값들의 구조체로 구성되어 있고
# 사실상 값만 바꾸는 게 어려운 일
# 그러나 이 문제에서는 단 하나의 값으로 구성된 단순한 연결리스트이고 값을 바꾸는 정도는 어렵지 않다
# list = 1 - 2 - 3 - 4
# cur = 1
# while cur and cur.next: -> 1, 2
# cur.val = cur.next.val -> 1 = 2
# cur.next.val = cur.val -> 2 = 1
# 2 -> 1
# cur = cur.next.next -> cur = 1.next.next == 3
# 3 = 4, 4 = 2
# 4 -> 3

# 2 - 1 - 4 - 3

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
