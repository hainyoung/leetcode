# from typing import List

# class Solution:
#     def reorderLogFiles(self, logs: List[str]) -> List[str]:
#         digits = []
#         letters = []
#         for log in logs:
#             if log.split()[1].isdigit():
#                 digits.append(log)
#             else:
#                 letters.append(log)
                
#         letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
                
#         return letters + digits
        

# class Solution:
#     def reorderLogFiles(self, logs: List[str]) -> List[str]:
#         digits = []
#         letters = []
#         for log in logs:
#             if log.split()[1].isdigt():
#                 digits.append(log) # 숫자인 로그는 digits에 append
#             else:
#                 letters.append(log) # 숫자가 아닐 경우엔 letters에 append
        
#         # 식별자는 순서에 영향을 끼치지 않지만,
#         # 문자가 동일할 경우 식별자 순으로 한다'는 조건에 맞추기 위해 다음의 코드 작성
#         # letters 재정렬
        
#         letters.sort(key=lambda x: (x.split()[1:], x.split()[0])) # [1:] 문자를 우선, 다음엔 식별자 기준 정렬

#         return letters + digits


# 03 Reorder Log Files
# 로그를 재정렬하라 기준은 아래와 같다
# 1. 로그의 가장 앞 부분은 식별자이다
# 2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다
# 3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일한 경우 식별자 순으로 한다
# 4. 숫자 로그는 입력 순서대로 한다

# input : logs = ["dig1 8 1 5 1", "let1 art ca", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
# output : ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]

# 요구 조건을 얼마나 깔끔하게 처리할 수 있는지를 묻는 문제
# 실무에서도 이 같은 로직은 자주 쓰이는 만큼 매우 실용적인 문제

# 먼저 문자로 구성된 로그가 숫자 로그보다 이전에 오며,
# 숫자 로그는 입력 순서대로 둔다
# 그렇다면, 문자와 숫자를 구분하고, 숫자는 나중에 그대로 이어 붙인다
# 로그 자체는 숫자 로그도 모두 문자열로 지정되어 있으므로, 타입을 확인하면 모두 문자로 출력된다
# 따라서 다음과 같이 isdigit()을 이용해서 숫자 여부인지를 판별해준다

# if log.split()[1].isdigit():
#     digits.append(log)

# else:
#     letters.append(log)

# 이 경우 숫자로 변호나 가능한 로그는 digits에, 그렇지 않은 경우 문자 로그는 letters에 추가된다
# 이제 문자 로그는 letters에 모두 모였으므로 다음과 같이 이를 제대로 정렬하기만 하면 된다

# letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
# 여기서는 식별자를 제외한 문자열 [1:]을 키로 하여 정렬,
# 동일한 경우에는 후순위로 식별자 [0]을 지정해 정렬되도록
# lambda expression, 람다 표현식을 이용해 정렬했다
# 다음, 모두 이어 붙여서 리턴한다
# return letters + digits

# + 연산자가 어떤 동작을 할까?
a = [1, 2, 3]
b = [4, 5, 6]

print(a + b) # [1, 2, 3, 4, 5, 6]
print(b + a) # [4, 5, 6, 1, 2, 3]


c = ["log2 1 3", "log1 art can", "log3 art works"]

for cc in c :
    print(cc.split()[1])


from typing import List
def reorderLogFiles(logs: List[str]):
    letters, digits = [], [] # 빈 리스트 2개 생성
    for log in logs:
        if log.split()[1].isdigit(): # ex)log.split()[1] : 8, art, 3, own, art
            digits.append(log)
        else:
            letters.append(log)
    
    # 2개의 key를 람다 표현식으로 정렬
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits

logs = ["dig1 8 1 5 1", "let1 art ca", "dig2 3 6", "let2 own kit dig", "let3 art zero"]

print(reorderLogFiles(logs))
# ['let1 art ca', 'let3 art zero', 'let2 own kit dig', 'dig1 8 1 5 1', 'dig2 3 6']

