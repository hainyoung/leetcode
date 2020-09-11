'''
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

###########################################################################
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

        if c in nums[i+1:]: # + 1 ? if target = 4, n = 2, nums[:] -> 2 + 2 = 4 -> not Two Sum
            return nums.index(n), nums[i+1:].index(c) + i + 1
'''

'''
# 3. imporve time complexity

# explanation
nums = [2, 7, 11, 15]
target = 9

nums_map = {}

for i, num in enumerate(nums):
    # change key & value and save as dictionary
    nums_map[num] = i # 2, 7, 11, 15 == key, index == value

# print(nums_map) # {2: 0, 7: 1, 11: 2, 15: 3}

# look up "target - first number" with a key
for i, num in enumerate(nums):
    if target - num in nums_map and i != nums_map[target - num]:
        print(nums.index(num), nums_map[target-num])
        
# loop 1:
# i == 0, num == 2
# if (1) 9-2 = 7 -> in nums_map (O)
# if (2) 0 != nums_map[7] (==1) -> 0 != 1 (O)
# return nums.index(2), nums_map[7] == 0, 1

# 위의 방법은 첫 번째 수를 뺀 결과 키 조회
# 비교, 탐색 대신 한 번에 정답을 찾는 방법으로 시간 복잡도를 개선할 수 있다

# 이 문제의 경우 타겟에서 첫 번재 수를 빼면 두 번째 수를 바로 알 수 있다
# 그렇다면 두 번째 수를 키로 하고 기존의 인덱스는 값으로 바꿔서 딕셔너리로 저장해두면
# 나중에 두 번째 수를 키로 조회해서 정답을 즉시 찾아낼 수 있음
# 이제 타겟에서 첫 번째 수를 뺀 결과를 키로 조회해보면
# 두 번째 수의 인덱스를 즉시 조회할 수 있다
# 딕셔너리는 해시 테이블로 구현되어 있고 이 경우 조회는 평균적으로 O(1)에 가능
# 최악의 경우 O(n)이 될 수도 있지만 말 그대로 최악의 경우이자 드문 경우

'''

# 4 improve the structure 

# explanation
nums = [2, 7, 11, 15]
target = 9

nums_map = {}

for i, num in enumerate(nums):
    if target - num in nums_map:
        print([nums_map[target - num], i])
    
    nums_map[num] = i # 왜 여기 위치해 있는지 답답했는데 하나씩 print 해 보니까 해결됨
    print(nums_map)

# {2: 0}
# [0, 1]
# {2: 0, 7: 1}
# {2: 0, 7: 1, 11: 2}
# {2: 0, 7: 1, 11: 2, 15: 3}  

# loop process
# loop 1 : i == 0, num == 2
# 9-2 == 7 in nums_map? no, nums_map = {} empty
# move on to the next 
# loop 2 : i == 1, num == 7
# 9-7 == 2 in nums_map? yes, nums_map = {2: 0}
# nums_map[target-num == 2], i == 1
# print [0, 1]
###############################################################################
