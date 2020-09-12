# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example
# Input:  [1,2,3,4]
# Output: [24,12,8,6]

# Note: Please solve it without division and in O(n).

from typing import List

def productExceptSelf(nums: List[int]):
    out = []
    p = 1
    for i in range(len(nums)):
        out.append(p)
        p = p * nums[i]

    p = 1
    for i in range(len(nums)-1, 0-1, -1):
        out[i] = out[i] * p
        p = p * nums[i]

    return out  