# 01. Valid Palindrome
# 주어진 문자열이 팰린드롬인지 확인하라, 대소문자 구분 X, 영문자와 숫자만을 대상으로 한다

# input : "A man, a plan, a canal: Panama"
# output : true

# input : "race a car"
# output : false

# sol1) list 

# step1) 문자열 입력 받아 알맞게 변환
'''
s = input()
strs = []
for char in s:
    if char.isalnum():
        strs.append(char.lower())

print(strs)
'''
# isalnum: alphabet, number 판별 함수, 해당하는 문자만 추가 
# 대소문자 구분 않으므로 lower()로 모두 소문자로 변환
# 입력값이 A man, a plan, a canal: Panama 일 때 
# strs 리스트는 
# ['a', 'm', 'a', 'n', 'a', 'p', 'l', 'a', 'n', 'a', 'c', 'a', 'n', 'a', 'l', 'p', 'a', 'n', 'a', 'm', 'a']'

# step2) 팰린드롬 여부 판별
'''
while len(strs) > 1 :
    if strs.pop(0) != strs.pop():
        print(False)
'''
# 파이썬의 리스트는 pop() 함수에서 인덱스를 지정할 수 있기 때문에
# 이처럼 0을 지정하면 맨 앞의 값을 가져올 수 있다
# 이렇게 맨 뒷부분의 pop() 결과와 매칭해 나가면서 일치하지 않는 경우 False를 출력한다
# 모두 통과했다면 True를 출력

# 함수로 정의
from dataclasses import dataclass
@dataclass
class Solution_1:
    def isPalindrome_1(self, s: str): # bool
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True

s_1 = 'race a car'
test_1 = Solution_1()
print(test_1.isPalindrome_1(s_1)) # False

# sol2) dque
# 리스트만으로도 충분히 문제를 해결할 수 있지만
# deque, 데크를 명시적으로 선언하면 좀 더 속도를 높일 수 있다

from collections import deque
def isPalindrome_2(s: str):
    # 자료형 deqeu로 선언
    strs: Deque = deque()

    for char in s:
        if char.isalnum():
            strs.apppend(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True

# 자료형을 데크로 선언하는 것만으로 시간이 단축
# 리스트 풀이 대비 거의 5배 가까이 속도 높임
# 리스트의 pop(0)은 O(n), 데크의 popleft()는 O(1)이기 때문에
# 각각 n번씩 반복하면 리스트 구현은 O(n^2), 데크 구현은 O(n)으로 성능차이가 큼


# sol3) Slicing
import re
def isPalindrome_3(s: str):
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1] # 슬라이싱 

#정규식으로 불필요한 문자를 필터링하고 문자열 조작하는 파이썬의 슬라이싱 사용
# 앞선 풀이에서는 isalnum()으로 모든 문자를 일일이 점검했다면
# 여기서는 문자열 전체를 한 번에 영숫자(Alphanumeric)만 걸러내도록 정규식으로 처리!
# 또한 파이썬은 문자열을 배열이나 리스트처럼 자유롭게 슬라이싱할 수 있는 좋은 기능을 제공하며
# [::-1]을 이용하면 뒤집을 수 있다
# 코드가 훨씬 더 줆어듦은 물론, 내ㅐ부적으로 C로 빠르게 구현되어 있어 훨씬 더 좋은 속도를 기대할 수 있다
# sol2에 비해 약 2배 정도 빠른 속도


# 문자열 슬라시이
# 파이썬에서는 문자열 슬라이싱이라는 매우 편리한 기능을 제공
# 무엇보다 내부적으로 매우 빠르게 동작
# 위치를 지정하면 해당 위치의 배열 포인터를 얻게 되며
# 이를 통해 연결된 객체를 찾아 실제 값을 찾아내는데, 이 과정은 매우 빠르게 진행되므로
# 문자열을 조작할 때는 항상 슬라이싱을 우선으로 사용하는 편이 속도 개선에 유리
# 문자열을 별도로 리스트로 매핑하는 등의 처리는 데이터 구조를 다루는 입장에선 좋은 방법이지만
# 별도 자료형으로 매핑하는 과정에서 상당한 연산 비용이 필요
# 전체적인 속도에서는 오히려 손해
# 대부분의 문자열 작업은 슬라이싱으로 처리하는 편이 가장 빠르다

sentence = '안녕하세요'
tmp = sentence[1:4]

print(sentence)
print(tmp)