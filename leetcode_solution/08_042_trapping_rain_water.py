from typing import List

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

# Example
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

# 1. two-pointer
def trap(height: List[int]):
    if not height:
        return 0

    volumne = 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right :
        left_max, right_max = max(height[left], left_max), max(height[right], left_max)

        if left_max <= right_max:
            volumne += left_max - height[left]
            left += 1

        else:
            volumne += right_max - height[right]
            right -= 1

    return volumne


# 2. stack
def trap(height: List[int]):
    stack = []
    volumne = 0

    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()

            if not len(stack):
                break
        
            distance = i - stack[-1] -1
            waters = min(height[i], height[stack[-1]]) - height[top]

            volumne ++ distance * waters
        stack.append()
    return volumne