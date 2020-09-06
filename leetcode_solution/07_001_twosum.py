# p. 173 07번 문제

# 1. Two Sum

# input : nums = [2 7, 11, 15], taget = 9
# output : [0, 1]
# explaination : nums[0] + nums[1] = 2 + 7 = 9

# coding interview 출제빈도 높음


from typing import List

def twoSum(self, nums: List[int], target: int):
    nums_map = {}
    for i, num in enumerate(nums): # index와 value 생성
        
        if target - num in nums_map:
            return [nums_map[target-num], i]
        
        nums_map[num] = i # 숫자를 넣으면 인덱스가 나오게 한다

nums = [2, 7, 11, 15]
target = 9

# nums_map = {}

# for i, num in enumerate(nums):
#     if target - num in nums_map:
#         print(nums_map[target-num], i)
#     nums_map[num] = i

# p. 173 풀이 1 : 브루트 포스로 계산
# 배열을 2번 반복하면서 모든 조합을 더해서 일일이 확인해보는 무차별 대입 방식 "브루트 포스, Brute-Force"

from typing import List
def twoSum1(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target :
                return [i, j]

a = twoSum1(nums, target)
print("a의 결과 :", a)

# 풀이 2 : in을 이용한 탐색
# 모든 조합을 비교하지 않고 정답 target에서 첫 번째 값을 뺀 값, target - n이 존재하는지 탐색하는 문제로 변경

def twoSum2(nums: List[int], target : int) -> List[int]:
    for i, n in enumerate(nums):
        complement = target - n # 탐색할 값 준비

        if complement in nums[i+1:]:
            return [nums.index(n), nums[i+1:].index(complement) + (i + 1)]

b = twoSum2(nums, target)
print("b의 결과 :", b)

# p. 175 풀이 3 : 첫 번째 수를 뺀 결과 키 조회



# p.176 풀이 4 : 조회 구조 개선

from dataclasses import dataclass
@dataclass
class Solution:
    def twoSum4(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums): # index와 value 생성
            
            if target - num in nums_map:
                return [nums_map[target-num], i]
            
            nums_map[num] = i # 숫자를 넣으면 인덱스가 나오게 한다

d = Solution()
print("d의 결과 :", d.twoSum4(nums, target))