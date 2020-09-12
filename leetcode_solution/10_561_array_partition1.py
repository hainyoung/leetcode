# Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

# Example
# Input: [1,4,3,2]

# Output: 4
# Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).

from typing import List

# 1. Ascending Order
def arrayPair1(nums: List[int]):
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []
    return sum

# 2. Even Number
def arrayPair2(nums: List[int]):
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i % 2 == 0:
            sum += n
    return sum

# 3. Pythonic way
def arrayPair3(nums: List[int]):
    return sum(sorted(nums)[::2])

    