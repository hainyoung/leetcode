from typing import List

# 1. Brute Force(Time Limit Exceeded)
# explanation
# [-4, -1, -1, 0, 1, 2]
# i    j    k ------>
# i        j   k---->
# i           j  k-->
# i j k pointers keep moving and find sum == zero
# 전체를 탐색한다
def threeSum1(nums: List[int]):
    results = []
    nums.sort() 

    for i in range(len(nums)-2):
        # skip duplicates
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, len(nums)-1):
            if j > i+1 and nums[j] ==  nums[j-1]:
                continue
            for k in range(j+1, len(nums)):
                if k > j+1 and nums[k] == nums[k-1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    results.append((nums[i], nums[j], nums[k]))

    return results

# duplicates?
# sort -> nums = [-4, -1, -1, 0, 1, 2]
# [-1(index1), 0, 1] / [-1(index2), 0, 1]

# nums = [-1, 0, 1, 2, -1, -4]
# print(threeSum1(nums))

# 2. Two-Pointer
# explanation
# i : axis
# [-4, -1, -1, 0. 1. 2]
#  i  left---> <--- right
#     sum < 0      sum > 0

def threeSum2(nums: List[int]):
    results = []
    nums.sort()

    # set "i" to the axis
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        # left --> , <-- right, calculate the sum
        left, right = i+1, len(nums)-1
        while left < right :
            sum = nums[i] + nums[left] + nums[right]

            if sum < 0:
                left += 1
            elif sum > 0 :
                right -= 1
            else:
                # sum = 0 -> correct answer and skip
                results.append((nums[i], nums[left], nums[right]))

                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -=1

    return results


# review 1002
