# 02 Reverse String

# 문자열을 뒤집는 함수를 작성하라, 입력값은 문자 배열, 리턴 없이 리스트 내부를 조작!
# input : ["h", "e", "l", "l", "o"]
# output : ["o", "l", "l", "e", "h"]

# sol1) Two Pointer, Swap
# Two Pointer를 이용한 전통적인 풀이방식
# 투 포인터 간단히 설명?
# 단어 그대로 2개의 포인터를 이용해 범위를 조정해가며 풀이하는 방식
# 여기서는 점점 더 범위를 좁혀가며 swap 하는 형태로 풀이할 수 있음
# 문제에서 '리턴 없이 리스트 내부를 직접 조작하라'는 제약 사항이 있으므로
# 다음과 같이 s 내부를 스왑 하는 형태로 풀이하면 된다
from typing import List

def reverseString_1(s:List[str]):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1



# sol2) pythonic way
# 파이썬의 기본 기능 이용하면 단 한 줄로 가능
# 이러한 방식을 흔히 파이썬다운 방식 "Pythonic Way"라고 한다
# 입력값이 리스트로 제공되므로 reverse() 함수를 사용하면 뒤집을 수 있다

def reverseString_2(s: List[str]):
    s.reverse()


s = ["h", "e", "l", "l", "o"]
s.reverse()

print(s) # ['o', 'l', 'l', 'e', 'h']

# reverse()는 리스트에만 제공된다
# 만약 입력값이 문자열이라면 앞서 살펴본 바와 같이
# 문자열 슬라이싱을 사용할 수 있다
# 슬라이싱은 리스트에도 사용할 수 있으며 성능 또한 매우 좋다


# s = s[::-1]
# 그러나 이 풀이는 리트코드에서는 오류가 발생
# 원래는 [::-1]도 정상적으로 처리되어야 하지만
# 이 문제의 경우 처리되지 않는데,
# 이 문제는 공간 복잡도를 O(1)로 제한하다보니
# 변수 할당을 처리하는 데 다소 제약이 있다
# 이 때 다음과 같은 트릭을 사용하면 잘 동작한다

# s[:] = s[::-1]
# 이런 트릭은 쉽게 알아내기 어려움
# 실제 코딩 테스트 시에도 이 같은 문제가 발생하면
# 디버깅에 애를 먹을 수 있으므로, 플랫폼의 특징에 대해 충분한 숙지가 필요

# 



##############################################################################################
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

#0926 review
