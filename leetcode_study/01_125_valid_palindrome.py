# deque 사용
import collections


def isPalindrome_4(s: str):
    stns: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            stns.append(char.lower())

    while len(stns) > 1 :
        if stns.popleft() != stns.pop():
            return False

    return True

a = "race a car"
b = "amama"

print(isPalindrome_4(a))
print(isPalindrome_4(b))


#################################################
# 슬라이싱과 정규식 사용
import re

# s = "race a car"
s = "abba"

s = s.lower()

s = re.sub('[^a-z0-9]', '', s)

print(s==s[::-1])