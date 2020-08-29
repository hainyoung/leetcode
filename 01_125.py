class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for c in s:
             if c.isalnum():
               strs.append(c.lower())
        # print(strs)
        
        while len(strs)>1:
            if strs.pop(0) != strs.pop(): # pop(0) : 맨 앞, pop() : 맨 끝
                return False
        return True


# deque를 활용

from collections import deque
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = deque()
        for c in s:
            if c.isalnum():
                strs.append(c.lower())
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True


'''
s = input()
strs = []

for char in s:
    if char.isalnum(): # 영어와 숫자만을 대상으로, isalnum() 함수를 사용한다
        strs.append(char.lower()) # strs라는 빈 리스트에 받은 문장의 요소들을 넣어두는데 이 때, 영어는 소문자로 모두 바꿔준다

print(strs)

while len(strs) > 1:  # strs의 길이가 하나가 되면 while문 escape
    if strs.popleft() != strs.pop(): # pop을 사용하면 하나씩 뽑아내고 없어짐, 이 성질을 이용해서 왼쪽, 오른쪽 끝 요소를 비교하고 
                                    # 다르면 False, 한 개 요소가 남을 때까지 모두 같으면 True를 반환
        return False
    return True

'''