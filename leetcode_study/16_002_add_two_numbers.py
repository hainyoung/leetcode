# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

from dataclasses import dataclass
@dataclass
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 1. data type conversion
# explanation
# 문제를 보자마자 먼저 생각나는 방법
# 연결 리스트를 문자열로 이어 붙인 다음 숫자로 변환, 계산한 후 다시 연결 리스트로 바꾼다
# 과정 자체도 복잡하고 게다가 역순으로 뒤집어야하기 때문에 시간이 많이 소요될 것
# 일단 시도는 해 본다
# 먼저 역순으로 연결 된 리스트를 뒤집어야 한다
# 앞선 문제에서 풀었던 코드를 사용하면 된다

# 1. data type converseion
# (1) reverse linked list
def reverseList(self, head: ListNode):
    node, prev = head, None
    
    while node:
        next, node.next = node.next, prev
        prev, node = node, next
        
    return prev

# ex) 2 - 4 - 3
# node = 2, prev = None
# while node:
# next = 2.next == 4
# 2.next = None -> 2 - Null
# prev = 2, node = next == 4
# while node:
# next = 4.next == 3
# 4.next = prev == 2 -> 4 - 2- Null
# prev = node == 4
# node = 3
# while node:
# next = 3.next == Null
# 3.next = prev == 4 -> 3 - 4 - 2 - Null
# while node? -> False
# return prev


# (2) linked list -> python list
def toList(self, node: ListNode):
    list: List =[]
    while node:
        list.append(node.val)
        node = node.next
    return list

# ex) 3 - 4 - 2
# [3, 4, 2]

# (3) python list -> linked list
def toReversedLinkedList(self, result: ListNode):
    prev: ListNode = None
    for r in result:
        node = ListNode(r)
        node.next = prev
        prev = node
        
    return node



# (4) add two linked lists
def addTwoNumbers1(self, l1: ListNode, l2: ListNode):
    a = self.toList(self.reverseList(l1))
    b = self.toList(self.reverseList(l2))
    
    resultStr = int(''.join(str(e) for e in a)) + \
                int(''.join(str(e) for e in b))
    
    return self.toReversedLinkedList(str(resultStr))

# a = self.toList(self.reversreList(2 - 4 - 3))
# a = self.toList(3 - 4 -2)
# a = [3, 4, 2]

# int(''.join(str(e) for e in a)) => 342

# 342 + 465 = 807
# self.toReversedLinkedList(807)
# prev = ListNode = None
# for r in result:
# node = ListNode(r)
# node = 8
# 8.next = prev == None
# prev = 8
# node = ListNode(r)
# node = 0
# 0.next = prev == 8
# prev = 0
# node = ListNode(r)
# node = 7
# 7.next = prev == 0
# prev = 7
# 7 - 0 - 8

# 2. using Full Adder
def addTwoNumbers2(self, l1: ListNode, l2: ListNode):
    root = head = ListNode(0)

    carry = 0
    while l1 or l2 or carry:
        sum = 0

        # add two input values
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next

        # quotient and remainder
        carry, val = divmod(sum+carry, 10)
        head.next = ListNode(val)
        head = head.next
    
    return root.next


# explanation
# l1 : 2 -4 - 3 / l2 : 5 - 6 - 4
# 일단, 연결리스트들의 합이 또 다른 연결리스트 형태가 되어야 하므로
# 연결리스트 하나를 만들어준다
# root = head = ListNode(0) 이렇게

# carry = 0 : 두 숫자의 합이 10 이상일 때 올라가야 하는 1의 값을 담아줄 수 있는 변수
# ex) 9 + 1 이면 carry에 1을 담아둠

# if l1: l1 == 2
# sum += 2
# l1 = 2.next == 4

# if l2 : l2 == 5
# sum(2) += 5 == 7
# l2 = 5.next == 6

# carry, val = divmod(7+0, 10) , divmod(a, b) -> a를 b로 나눴을 때의 몫과 나머지를 반환
# carry = 0, 7 ( 7 / 10) -> 몫: 0, 나머지 : 7
# head.next  - 7 -> 0 - 7
# head = head.next == 7

# l1 = 4, l2 = 6, caryy = 0
# sum  = 0
# sum += 4
# sum += 6 -> sum == 10
# caryy, val = divmod(10, 10)
# carry = 1, val = 0
# head.next = ListNode(0)
# 7. next == 0
# head = 0

# l1 = 3, l2 = 4, caryy = 1
# sum += 3
# sum += 4 -> sum = 7
# cayy, val = divmod(7 + 1, 10)
# cayy = 0, val = 8
# head.next = ListNode(8)
# 0.next = 8 -> 0 - 7 - 0 - 8
# head = 8

# root = 0
# return root.next
# 7 - 0 - 8



# 숫자형 리스트를 단일 값으로 병합하기
# 