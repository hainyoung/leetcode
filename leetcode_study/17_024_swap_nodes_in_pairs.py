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

# 단순 값만 바꾸는 일에 비해 연결리스트 자체를 바꾸는 일은 다소 복잡
# 1 -> 2 -> 3 -> 4 -> 5 - > 6 이라는 연결 리스트가 있을 경우
# 3 -> 4로, 4 -> 3으로 바꾼다고 할 때 단순히 둘만 바꾸면 되는 게 아니라
# 그 앞인 2가 가리키는 연결 리스트와 5로 연결되는 연결 리스트도 같이 변경해야 하기 때문
# 2는 4와 연결되고 5는 3과 연결되어야 하니...
# b = a.next
# a.next = b.next
# b.next = a
# 이렇게 b가 a를 가리키고 a는 b의 다음을 가리키도록 변경
# 그러나 이게 다가 아니다
# prev.next = b
# a = a.next
# prev = prev.next.next
# a의 이전 노드가 b를 가리키게 하고
# 다음번 비교를 위해 prev는 두 칸 앞으로 이동한다
# 그리고 다시 다음번 교환을 진행...

# 위의 답으로 풀어보자면
# root = prev = ListNode(None) : Null ->
# list : 1 - 2 - 3 - 4
# prev.next = head -> Null.next = 1 -> Null -> 1

# while head and head.next
# b가 a(head)를 가리키도록 할당 (allocate b to point 'a(head)')
# b = head.next -> b = 1.next , b == 2
# head.next = b.next
# 1.next = 2.next -> 1.next = 3 : 1 -> 3
# 2.next = head -> 2 - 1 - 3

# prev가 b를 가리키도록 할당( allocate prev to point 'b')
# prev.next = b
# Null.next = 2 -> Null -> 2
# 다음번 비교를 위해 이동 (move for comparing)
# head = head.next -> head = 3
# prev = prev.next.next -> 2.next -> prev == 1

# while head and head.next(3 , 4)
# b = 3.next -> b == 4
# 3.next = 4.next -> 3 -> Null
# 4.next = 3 -> 4 -> 3

# prev.next = b
# 1.next = 4 -> 1 -> 4 -> 3 -> Null

# Null(root) - 2 - 1 - 3 - 4

# return root.next

#  2 - 1 - 3 - 4





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
