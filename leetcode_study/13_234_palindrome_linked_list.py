# Given a singly linked list, determine if it is a palindrome.

# Example

# Input: 1->2
# Output: false

# Input: 1->2->2->1
# Output: true

# Follow up:
# Could you do it in O(n) time and O(1) space?
from typing import List

# 1. covert to list
# explanation
# 팰린드롬 여부를 판별하기 위해서는 앞뒤로 모두 추출할 수 있는 자료구조가 필요
# 일반적인 스택 자료구조는 마지막 요소만 추출하는 연산만 있지만
# 파이선의 리스트는 pop() 함수에 인덱스를 지정할 수가 있어서
# 마지막 요소가 아니라도 얼마든지 원하는 위치를 자유롭게 추출할 수 있다
# 따라서 이 문제는 연결 리스트를 파이썬의 리스트로 변환하여
# 리스트의 기능을 이용하면 쉽게 풀이할 수 있다
# 자유롭게 인덱스를 지정할 수 있는 파이썬 리스트의 강력함을 확인!

def isPalindrome1(head: ListNode):
    q: List = []
    # if head is empty->return True
    if not head:
        return True

    node = head
    # convert to list
    while node is not None:
        q.append(node.val)
        node = node.next

    # discriminate palindrome
    while len(q) > 1 :
        if q.pop(0) != q.pop():
            return False

    return True

# 2. optimization using deque
# explanation
# 위의 코드 중 if 1.pop(0) != q.pop():
# 여기서의 문제점은 q.pop(0)에서 첫 번째 아이템을 추출할 때의 속도이다
# 동적 배열로 구성된 리스트는 맨 앞 아이템을 가져오기에 적합한 자료형이 아니다
# 왜냐하면 첫 번째 값을 꺼내오면 모든 값이 한 칸씩 shifting, 이동되며
# 시간 복잡도 O(n)이 발생하기 때문이다
# 이 때문에 최적화를 위해서는 맨 앞의 데이터를 가져올 때 O(n) 이내에 처리할 수 있는 자료형이 필요
# 파이썬의 deque는 이중 연결 리스트 구조로 양쪽 방향 모두 추출하는데 시간 복잡도가 O(1)에 실행된다

# 만약 리스트로 처리했을 때 타임아웃이 발생하거나 오프라인 코딩 인터뷰에서 면접관이
# 이렇게 하면 과연 효율적인가요? 라고 질문한다면
# 양방향 모두 O(1)에 가능한 데이크를 설명한 다음 이 자료형을 적용할 것이라고 이야기해 볼 수 있다
# 파이선에서 리스트를 데크로 수정하려면 딱 2군데만 수정하면 되는 간단한 작업이다

# q: Deque = collections.deque()
# if q.popleft() != q.pop():
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







# # 예제 1
# if __name__ == '__main__':
#     li_1 = ListNode(1)
#     li_2 = ListNode(2)
#     li_1.next = li_2

#     a = Solution()
#     aaa = a.isPalindrome(li_1)
#     print(aaa)

# # 예제 2
# if __name__ == '__main__':
#     li_1 = ListNode(1)
#     li_2 = ListNode(2)
#     li_3 = ListNode(2)
#     li_4 = ListNode(1)
#     li_1.next = li_2
#     li_2.next = li_3
#     li_3.next = li_4

#     b = Solution()
#     bbb = b.isPalindrome(li_1)
#     print(bbb)