# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
# Example 4:

# Input: s = "([)]"
# Output: false
# Example 5:

# Input: s = "{[]}"
# Output: true

# 전형적인 스택 문제 , 매우 쉬우면서도 기본기 점검할 수 있는 좋은 문제
# (, [, { 은 스택에 push 하고 ), ], }을 만날 때 스택에서 pop한 결과가
# 매핑 테이블(Mapping Table) 결과와 매칭되는지 확인하면 된다
# 여기서는 먼저 매핑 테이블을 만들어놓고 테이블에 존재하지 않으면 무조건 push,
# pop() 했을 때 결과가 일치하지 않으면 False를 return 하도록 다음과 같이 구현

def isValid(self, s: str):
    stack = []
    table = {
        ')': '(',
        '}': '{',
        ']': '[',
    }


    # using stack and checking for a match
    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop(): # exception handling
            return False
        
        # else == char in stack or table[char]== stack.pop()

        return len(stack) == 0

# explanation
# ! Key의 Value를 얻기 위해서는 딕셔너리변수이름[Key]를 사용한다 ! #


# s = ()[]{}

# loop1
# ( is not in table -> stack.append('(') -> stack = ['(']

# loop2
# ) , table[')'] == stack.pop()
# table[')'] == ')'의 value, '(' == stack.pop()

# 헷갈렸던 점, )은 pop이 안 되는 것 아닌가?
# 해결 : )는 stack에 append된 적이 없다!
# 따라서 비교 과정만 거치고 기존 stack에 append 되어 있던 '('는 사라짐
# 결론적으로 ()가 들어오면 stack은 비게 된다

# loop3, 4, 5, 6 마찬가지로 진행됨

# 위 코드는 pop() 결과가 일치하지 않는지 확인하는 것 플러스
# 스택이 비어있는지를 최종적으로 확인해서 True, False를 결정(len(stack) == 0)

# 예외 처리가 중요하다!



'''
# elif table[char] != stack.pop():
#     return False
# 풀어쓰면

# if table[char] != stack.pop():
#    return False
# else  table[char] == stack.pop():
    #  return true

# Stack과 Queue


stack = []

stack.append(1) 
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)

while stack :
    print(stack.pop())

print()
print()

q = []

q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)

while q:
    print(q.pop(0)) 


print()
print()

# 위와 같이 써도 되지만 시간 복잡도가 높아진다

import collections
qu = collections.deque()

qu.append(1)
qu.append(2)
qu.append(3)
qu.append(4)
qu.append(5)

print(qu.popleft()) # O(1)


a = [[[0] * 4] * 3]
print(a)
'''