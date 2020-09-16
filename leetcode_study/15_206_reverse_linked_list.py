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
            if not node: # (1)
                return prev

            next, node.next = node.next, prev
            return reverse(next, node)
        
        return reverse(head)

# explanation 
# input 1 - 2 - 3 - 4 - 5 - NULL
# node : 1, prev : none
# (1) 충족 x
# next, 1.next = 1.next, none
# next = 2 , 1.next = none -> (1 - null)
# recursiv! : reverse(2, 1)

# node : 2, prev : 1
# if x
# next, 2.next = 2.next, 1
# next = 3, 2.next = 1 -> (2 - 1 - null)
# reverse(3, 2)

# node : 3, prev : 2
# if x
# next, 3.next = 3.next, 2
# next = 4, 3.next = 2 -> (3 - 2 - 1 - null)
# reverse(4, 3)

# node : 4, prev : 3
# if x
# next, 4.next = 4.next, 3
# next = 5, 4.next = 3 -> (4 - 3 - 2 - 1 - null)
# reverse(5, 4)

# node : 5, prev : 4
# if x
# next, 5.next = 5.next, 4
# next = null, 5.next = 4 -> (5 - 4 - 3- 2 - 1 - null)
# reverse(none, 5)

# if O
# return prev (5 - 4 - 3 - 2 - 1 - null)

# return reverse(head) (최종 적용)

# 2. iterative

def reverseList2(self, head: ListNode):
    node, prev = head, None

    while node:
        next, node.next = node.next, prev

        node, prev = next, node

    return prev

# exlpanation
# 1 -2 - 3- 4- 5
# node, prev = 1, None
# while node:
# next, 1.next = 1.next, None
# next = 2, 1.next = None
# node, prev = 2, 1
# 
# while node:
# next, 2.next = 2.next, 1
# next = 3, 2.next = 1
# node, prev = 3, 2
# ...
# return prev : 5 - 4- 3- 2- 1
# 

# 1, 2는 비슷한 속도를 보인다
# 다만 반복이 재귀에 비해 70% 수준의 메모리를 차지해 공간 복잡도는 낮은 편
# # 실행 속도도 약간 더 빠름 
