# 21
# Definition for singly-linked list.

from dataclasses import dataclass

@dataclass
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

@dataclass
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1

        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1


def printAll(head):
    start = head
    while start :
        print(start.val)
        start = start.next

if __name__ == '__main__':
    l1_1 = ListNode(1)
    l1_2 = ListNode(2)
    l1_3 = ListNode(4)
    l1_1.next = l1_2
    l1_2.next = l1_3

    l2_1 = ListNode(1)
    l2_2 = ListNode(3)
    l2_3 = ListNode(4)
    l2_1.next = l2_2
    l2_2.next = l2_3

    s = Solution()
    result = s.mergeTwoLists(l1_1, l2_1)

    printAll(result)
    
stack = []



'''
node1 = ListNode(1)
node1.next = node2 = ListNode(2)
node2.next = node3 = ListNode(4)


연결 리스트 하나씩 조회해서 출력하기

node = node1
while node: # node가 존재할 때까지 loop를 돈다
    print(node.val, end=' ')
    node = node.next


# 중간 원소 지우기
node1.next = node1.next.next

'''