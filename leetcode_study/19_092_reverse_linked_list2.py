# Reverse a linked list from position m to n. Do it in one-pass.

# Note: 1 ≤ m ≤ n ≤ length of list.

# Example:

# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL

from dataclasses import dataclass
@dataclass
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(self, head: ListNode, m: int, n: int):
    # for excpetion
    if not head or m==n:
        return head

    root = start = ListNode(None)
    root.next = head
    
    # set 'start' and 'end'
    for _ in range(m - 1):
        start = start.next

    end = start.next

    for _ in range(n - m):
        tmp, start.next, end.next = start.next, end.next, end.next.next
        start.next.next = tmp
    
    return root.next
    
# explanation
# ex) 1 -> 2 -> 3 -> 4 -> 5
# m = 2, n = 4 : 1 -> 4 -> 3 -> 2 -> 5

# root = start = ListNode(None) : root
# root.next = head : root -> 1 -> 2 -> 3 -> 4 -> 5

# for _ in range(m-1) == for _ in range(1)
# loop 1
# start = start.next : start = root.next == 1
# end = staet.next == 1.next == 2

# for _ in range(n-m) == for _ in range(2)

# loop1
# tmp = start.next == 1.next == 2
# start.next = end.next == 2.next == 3
# end.next = end.next.next == 2.next.next == 4
# start.next.next = tmp == 2

# root - 1 - 2 - 3 - 4 - 5
# root - 1 - 3 - 2 - 4 - 5
# start : 1, tmp : 2, end : 2

# loop2
# tmp = star.next == 1.next == 3
# start.next = end.next == 2.next == 4
# 1 -> 4
# end.next = end.next.next == 2.n.n == 5
# start.next.next = tmp == 3
# 1 -> 4 -> 3 -> 2 -> 5
