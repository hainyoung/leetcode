# Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

# Example 1:

# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL
# Example 2:

# Input: 2->1->3->5->6->4->7->NULL
# Output: 2->3->6->7->1->5->4->NULL

# 주의
# 값의 홀짝 여부가 아닌
# 노드의 자릿값의 홀짝 여부를 따지는 것임

# 1. using repetitive structure

def oddEvenList(self, head: ListNode):
    # for exception
    if head is None:
        return None

    odd = head
    even = head.nexxt
    even_head = head.next

    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next

    odd.next = even_head
    return head


# explanation
# ex) 1 - 2 - 3 - 4 - 5
# odd = 1, even = 1.next = 2
# even_head = 1.next = 2

# while even and even.next: -> 2, 3
# odd.next = 1.n.n = 3
# even.next = 2.n.n = 4
# 1 -> 3, 2 -> 4
# odd = 3, even = 4

# while even and even.next: -> 4, 5
# odd.next = 3.n.n = 5
# even.next = 4.n.n = None
# 3 -> 5, 4 -> None
# odd = 5, even = 4

# while -> False

# odd.next = even_head
# 5.next = 2
# 1 -> 3 -> 5 -> 2 -> 4 -> None
