# # Definition for singly-linked list.

# 234. Palindrome Linkedlist

from dataclasses import dataclass
@dataclass
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

@dataclass
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q: List = []

        if not head:
            return True

        node = head

        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next
        
        # 팰린드롬 판별
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
        
        return True

# 예제 1
if __name__ == '__main__':
    li_1 = ListNode(1)
    li_2 = ListNode(2)
    li_1.next = li_2

    a = Solution()
    aaa = a.isPalindrome(li_1)
    print(aaa)

# 예제 2
if __name__ == '__main__':
    li_1 = ListNode(1)
    li_2 = ListNode(2)
    li_3 = ListNode(2)
    li_4 = ListNode(1)
    li_1.next = li_2
    li_2.next = li_3
    li_3.next = li_4

    b = Solution()
    bbb = b.isPalindrome(li_1)
    print(bbb)