# Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

# Example 1:

# Input: "bcabc"
# Output: "abc"
# Example 2:

# Input: "cbacdcbc"
# Output: "acdb"

from dataclasses import dataclass
import collections


# 1. recursive
@dataclass
class Solution1:
    def removeDuplicateLetters1(self, s: str):
        # 1. recursive
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''
    

# 2. using Stack
@dataclass
class Solution2:
    def removeDuplicateLetters2(self, s: str):
        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue

            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return ''.join(stack)