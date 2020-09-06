from collections import deque

N, K = map(int, input().split())

d = deque(range(1, N+1)) # 1번부터 N까지 queue에 들어간다
ans = list()

while len(d) > 0 : # == while len(d): 이렇게 써도 된다
    d.rotate(-K+1)
    ans.append(d.popleft()) # pop()은 맨 뒤(오른쪽), popleft()는 맨 앞

# rotate : 회전하다
# 요세푸스 순열 : 회전하는 느낌이다
# 빼고 뒤로 붙여주는 과정이 파이썬에 존재
# rotate는 방향이 중요
# 뒤에 있는 것을 앞에 붙여줌
# if, d.rotate(K-1)을 하면 뒤에 있는 순서대로 두 개가 앞에 붙여짐
# 현재는 앞부터 첫번째 두번째가 뒤로 가서 붙어야 하므로
# -K +1, -2를 넣어줘야 한다

# print(str(ans)[1:-1]) # 3, 6, 2, 7, 5, 1, 4

# print(type(str(ans)[1:-1]))

print(f"<{str(ans)[1:-1]}>") # <3, 6, 2, 7, 5, 1, 4>

# f-string

# format형
# print("{} is apple".format('apple'))

# f-string 형
# apple = 'apple'
# print(f'{apple}')