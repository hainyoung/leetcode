

from typing import List

# two pointer 사용
def reverseString_1(s: List[str]):
    left, right = 0, len(s)-1

    while left < right : # left == right 인 경우에는 그냥 그대로 있으면 됨
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

        # return s # return 없이 내부 직접 조작

# s = list(input().split())

# print(s)
# print(reverseString_1(s)) # return 값이 없어서 None으로 출력됨

# pyhonic
def reverseString_2(s: List[str]):
    s.reverse()
    return s

s2 = list(input().split())
print(reverseString_2(s2))