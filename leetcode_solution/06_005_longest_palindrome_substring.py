# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Input: "cbbd"
# Output: "bb"

# pointer expansion
def longestPalindrome(s: str):
    def expand(left: int, right :int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        return s[left+1:right]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    for i in range(len(s) - 1):
        result = max(result, expand(i, i), expand(i, i+1), key=len)
    return result

