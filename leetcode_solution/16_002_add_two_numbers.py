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


# 1. data type converseion
# (1) reverse linked list
def reverseList(self, head: ListNode):
    node, prev = head, None
    
    while node:
        next, node.next = node.next, prev
        prev, node = node, next
        
    return prev

# (2) linked list -> python list
def toList(self, node: ListNode):
    list: List =[]
    while node:
        list.append(node.val)
        node = node.next
    return list

# (3) python list -> linked list
def toReversedLinkedList(self, result: ListNode):
    prev: ListNode = None
    for r in result:
        node = ListNode(r)
        node.next = prev
        prev = node
        
    return node

# (4) add two linked lists
def addTwoNumbers(self, l1: ListNode, l2: ListNode):
    a = self.toList(self.reverseList(l1))
    b = self.toList(self.reverseList(l2))
    
    resultStr = int(''.join(str(e) for e in a)) + \
                int(''.join(str(e) for e in b))
    
    return self.toReversedLinkedList(str(resultStr))


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