# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example
# Input:  [1,2,3,4]
# Output: [24,12,8,6]

# Note: Please solve it without division and in O(n).
# 쉽게 생각할 수 있는 풀이법을 제한함
# 전체 곱셈 값을 구해놓고 각 항목별로 자기 자신을 나눠 풀이한느 방법은 NO
from typing import List
# 1. 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
# explanation
# nums = [1, 2, 3, 4]
#       ------------->
# p = 1   1  2  6 
# out = [1, 1, 2, 6]
# nums = [1, 2, 3, 4]
#     < -------------
#        24, 12, 4, 1 = p
# out * p
# out = [24, 12, 8, 6]

def productExceptSelf(nums: List[int]):
    out = []
    p = 1
    # 왼쪽 곱셈
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]

    p = 1
    # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
    for i in range(len(nums)-1, 0 - 1, -1):
    # index의 특성상 0번까지 포함시키려면 -1로 명시해줘야함
    # 따라서 0 - 1 이 나오고 for문의 range(x, y, z)에서 z는 증분을 지정하는 파라미터
    # 1씩 줄어들어야하기 때문에 -1이 들어감
        out[i] = out[i] * p
        p = p * nums[i]

    return out

# 첫번째 for문 ( i = 0, 1, 2, 3)
# loop1 
# i = 0
# out.append(1) => out = [1]
# p = 1*num[0] = 1*1 = 1

# loop2
# i = 1
# out.append(p=1) => out = [1, 1]
# p = 1 * nums[1] = 1 * 2 = 2

# loop3
# i = 2
# out.append(p=2) => out = [1, 1, 2]
# p = 2 * nums[2] => 2 * 3 = 6

# loop4
# i = 3
# out.append(p=6) => out = [1, 1, 2, 6]
# p = 6 * nums[3] = 6 * 4 = 24

# out = [1, 1, 2, 6]
# p = 1 초기화
# 두번째 for문 (i = 3, 2, 1, 0)
# loop1
# i = 3
# out[3] = out[3] * 1 = 6 * 1 = 6
# p = 1 * nums[3] = 1 * 4 = 4

# loop2
# i = 2
# out[2] = out[2] * 4 = 2 * 4 = 8
# p = 4 * nums[2] = 4 * 3 = 12

# loop3
# i = 1
# out[1] = out[1] * 12 = 1 * 12 = 12
# p = 12 * nums[1] = 12 * 2 = 24

# loop4
# i = 0
# out[0] = out[0] * 24 = 1 * 24 = 24
# p = 24 * nums[0] = 24 * 1 = 24

# out [0] = 24, out[1] = 12, out[2] = 8, out[3] = 6
# out = [24, 12, 8, 6]
