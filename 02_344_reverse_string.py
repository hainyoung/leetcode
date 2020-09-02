from typing import List

# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         s.reverse()


# class Solution:
def reverseString(self, s: List[str]) -> None:

    p, q = 0, len(s) - 1 
    while p < q :
        s[p], s[q] = s[q], s[p]
        p += 1
        q -= 1


        
