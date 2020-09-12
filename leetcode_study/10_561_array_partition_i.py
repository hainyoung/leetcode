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

# min()을 합산 했을 때 최대를 만드는 것은 결국 min(a, b)이 되도록 커야 한다는 의미
# a, b 간 차이가 작게 정렬한 후 페어를 만들어야 최대가 나온다

def arrayPairSum1(nums: List[int]):
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
# 위의 방식은 pair에 대해 일일이 min() 값을 구함
# 그렇게 하지 않아도 짝수 번째 값(인덱스 0부터 시작하니까)을 더하면 된다
# 정렬된 상태에서는 짝수 번째에 항상 작은 값이 위치하기 때문
# 불필요한 리스트 변수를 생략할 수 있기 때문에 전체 코드가 많이 줄어들어 간결하게 구현 가능

def arrayPairSum2(nums: List[int]):
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i % 2 == 0:
            sum += n
    return sum

# 3. pythonic
# 위의 코드보다 더 간결히?
# 슬라이싱을 활용하면 된다 -> Pythonic way

def arrayPairSum3(nums: List[int]):
    return sum(sorted(nums)[::2])

nums = [1, 2, 3, 4]
print(nums[::2])