# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Input: nums = [3,3], target = 6
# Output: [0,1]

# 1. Brute-Force
from typing import List

def twoSum1(nums: List[int], target: int):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# 2. search with 'in'
def twoSum2(nums: List[int], target: int):
    for i, n in enumerate(nums):
        c = target - n # c : complement

        if c in nums[i+1:]: 
            return [nums.index(n), nums[i+1:].index(c) + i + 1]

# 3. improve the time complexity
def twoSum3(nums: List[int], target: int):
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target-num]:
            return [nums.index(num), nums_map[target-num]]


# 4. imporove the structure
def twoSum4(nums: List[int], target: int):
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        
        nums_map[num] = i


# 5. two-pointer
def twoSum5(nums: List[int], target: int):
    left, right = 0, len(nums) -1
    while not left == right :
        if nums[left] + nums[right] < target :
            left +=1
        elif nums[left] + nums[right] > target :
            right -= 1
        else :
            return left, right
