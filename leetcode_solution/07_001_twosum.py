# 1. Brute-Force
from typing import List

def twoSum1(nums: List[int], target: int):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# 2. search with 'in'
def twoSume2(nums: List[int], target: int):
    for i, n in enumerate(nums):
        c = target - n # c : complement

        if c in nums[i+1:]: 
            return nums.index(n), nums[i+1:].index(c) + i + 1

