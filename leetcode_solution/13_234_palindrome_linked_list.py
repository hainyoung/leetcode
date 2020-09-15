# Given a singly linked list, determine if it is a palindrome.

# Example

# Input: 1->2
# Output: false

# Input: 1->2->2->1
# Output: true

# Follow up:
# Could you do it in O(n) time and O(1) space?



from typing import List
from dataclasses import dataclass
@dataclass
class LitNode:
    def __init__(self, val=0, nex=None):
        self.val = val
        self.next = next


def isPalindrome1(head: ListNode):
    # creat an empty list
    q: List = []

    # if head doesn't exist, return True
    if not head:
        return True

    node = head
    # convert to list
    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False

    return True


# 2. optimization using deque
import collections
def isPalindrome2(head: Listnode):
    # declare "deque"
    q: Deque = collections.deque()

    if not head:
        return True

    node = head
    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1 :
        if q.popleft() != q.pop():
            return False
    return True




