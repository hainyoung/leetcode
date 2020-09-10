# Write a function that reverses a string. The input string is given as an array of characters char[].

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# You may assume all the characters consist of printable ascii characters.

# Example

# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

# 1. twopointer , swqp
from typing import List
def reverseString1(s: List[str]):
    left, right = 0, len(s) - 1
    while left < right :
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


# 2. pythonic
def reverseString2(s: List[str]):
    s.reverse()
    