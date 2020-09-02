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