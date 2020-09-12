# Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

# Example
# Input: [1,4,3,2]

# Output: 4
# Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).

from typing import List

# 1. Ascending Order
# explanation
# 1 2 3 4
# case 1 : (1, 2), (3, 4) -> min(1, 2), min(3, 4) -> 1 + 3 = 4
# case 2 : (1, 3), (2, 4) -> min(1, 3), min(2, 4) -> 1 + 2 = 3
# case 3 : (1, 4), (2, 3) -> min(1, 4), min(2, 3) -> 1 + 2 = 3

def arrayPairSum1(nums: Lit[int]):
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []

    return sum

# sort -> nums : [1, 2, 3, 4]
# loop 1
# n = 1 , pair = [1]
# n = 2, pair = [1, 2] -> len(pair) == 2, sum += min(1, 2) -> sum = 1
# pair = [] empty
# n = 3, pair = [3]
# n = 4, paier = [3, 4] -> len(pair) == 2, sum += min(3, 4) -> sum = 1 + 3 = 4
# return 4

# 2. even number

# 3. pythonic
