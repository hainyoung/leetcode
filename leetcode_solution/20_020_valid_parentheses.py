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

def isValid(self, s: str):
    stack = []
    table = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char not in table:
            stack.append(char)

        elif not stack or table[char] != stack.pop():
            return False

    return len(stack) == 0

    