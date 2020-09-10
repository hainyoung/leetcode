# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome

# Example
# Input: "A man, a plan, a canal: Panama"
# Output: true

# Input: "race a car"
# Output: false

# Constraints
# s consists only of printable ASCII characters.

# 1. list
def isPalindrome1(s: str):
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1 :
        if strs.pop(0) != strs.pop():
            return False
    return True


# 2. deque
import collections
def isPalindrome2(s: str):
    strs: Deque = collections.deque()

    for char in s :
        if char.isalnum():
            strs.append(char.lower())
    
    while len(strs) > 1 :
        if strs.popleft != strs.pop():
            return False
    
    return True


# 3. slicing
import re
def isPalindrome3(s: str):
    s = s.lower()

    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]
    