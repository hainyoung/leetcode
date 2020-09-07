# # deque 사용
# import collections


# def isPalindrome_4(s: str):
#     stns: Deque = collections.deque()

#     for char in s:
#         if char.isalnum():
#             stns.append(char.lower())

#     while len(stns) > 1 :
#         if stns.popleft() != stns.pop():
#             return False

#     return True

# a = "race a car"
# b = "amama"

# print(isPalindrome_4(a))
# print(isPalindrome_4(b))


# #################################################
# # 슬라이싱과 정규식 사용
# import re

# # s = "race a car"
# s = "abba"

# s = s.lower()

# s = re.sub('[^a-z0-9]', '', s)

# print(s==s[::-1])

#######################################################################
'''
# 일반 리스트
def Palindrome_1(s: str):
    strs = []

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


# Deque 자료형 사용
import collections

def Palindrome_2(s:str):
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True

'''
# 정규식 표현과 슬라이싱 사용
import re

def Palindrome_3(s: str):
    s = s.lower()

    s = re.sub(r'[^a-z0-9]', '', s)

    return s == s[::-1]

s = 'ama'

print(Palindrome_3(s))