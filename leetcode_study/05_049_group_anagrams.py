# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Input: strs = [""]
# Output: [[""]]

# Input: strs = ["a"]
# Output: [["a"]]

# 정렬하여 딕셔너리에 추가
# 에너그램을 판단하는 가장 간단한 방법은 정렬하여 비교하는 것
# 에너그램 관계인 단어들을 정렬하면, 서로 같은 값을 갖게 되기 때문
# sorted()는 문자열도 잘 정렬하며 결과를 리스트 형태로 리턴하는데
# 이를 다시 키로 사용하기 위해 join()으로 합쳐 이 값을 키로 하는 딕셔너리로 구성
# 에너그램끼리는 같은 키를 갖게 되고 따라서 여기에 append() 하는 형태가 된다
# 딕셔너리는 키/값 해시 테이블 자료형이다

strs = ["eat","tea","tan","ate","nat","bat"]

import collections
anagrams = collections.defaultdict(list)

print(anagrams) # defaultdict(<class 'list'>, {})

# for word in strs:
#     anagrams[''.join(sorted(word))].append(word)
#     print(anagrams)

# defaultdict(<class 'list'>, {'aet': ['eat']})
# defaultdict(<class 'list'>, {'aet': ['eat', 'tea']})
# defaultdict(<class 'list'>, {'aet': ['eat', 'tea'], 'ant': ['tan']})
# defaultdict(<class 'list'>, {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan']})
# defaultdict(<class 'list'>, {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']})  

# for word in strs:
#     print(sorted(word))
# ['a', 'e', 't']
# ['a', 'e', 't']
# ['a', 'n', 't']
# ['a', 'e', 't']
# ['a', 'n', 't']
# ['a', 'b', 't']
for word in strs:
    print(''.join(sorted(word)))
# aet
# aet
# ant
# aet
# ant
# abt

from typing import List
def groupAnagrams(strs: List[str]):
    anagrams = collections.defaultdict(list) # default값이 lsit

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)

    return anagrams.values()

# strs = ["eat","tea","tan","ate","nat","bat"]
# process
# 1 step : sorted(word), 2 step : ''.join , 3 step : .append(word)
# roop 1
# eat -> 'a', 'e', 't' -> 'aet', anagrams[aet].append(eat)
# anagrams : {'aet' : ['eat']}
# roop 2
# tea -> 'a', 'e', 't' -> 'aet', anagrams[aet].append(tea)
# anagrams : {'aet' : ['eat', 'tea']}
# roop 3
# tan -> 'a', 'n', 't' -> 'ant', anagrams[ant].append(tan)
# anagrams : {'aet' : ['eat', 'tea'], 'ant' : ['tan']}
# ...

# 여러 가지 정렬 방법
# 파이썬은 정렬 함수를 기본으로 제공

# sorted
a = [2, 5, 1, 9, 7]
print(sorted(a)) # [1, 2, 5, 7, 9]

b = 'zbdaf'
print(sorted(b)) # ['a', 'b', 'd', 'f', 'z']

# 숫자, 문자 정렬 가능
# sorted(list) 순서대로 정렬한 리스트를 결과로 리턴
# 다시 문자열로 결합하려면
print(''.join(sorted(b))) # abdfz

# sorted() 라는 별도 함수 외에도 리스트 자료형은 sort() 메소드를 함께 제공함
# 리스트 자체를 정렬할 수 있다
# 이를 제자리 정렬, In-place Sort 라고 한다
# 일반적으로 제자리 정렬 알고리즘은 입력을 출력으로 덮어 쓰기 때문에
# 별도의 추가 공간이 필요하지 않으며 리턴값이 없다
# 따라서 정렬 결과를 별도로 리턴하는 sorted()와는 다르므로 주의!

# alist.sort() : 리스트 자체를 제자리 정렬
# alist = blist.sort() # 잘못된 구문
# sort() 함수는 None을 리턴하므로 주의!

# sorted()는 또한 key= 옵션을 지정해 정렬을 위한 키 또는 함수를 별도 지정 가능
# 다음 코드는 정렬을 위한 함수로 길이를 구하는 len을 지정
c = ['ccc', 'aaaa', 'd', 'bb']
print(sorted(c, key=len)) # ['d', 'bb', 'ccc', 'aaaa']
# 길이 순서로 정렬된다

# 함수를 이용해 키를 정의하는 방법을 좀 더 살펴보자
# 다음은 함수를 이용해 첫 문자열과 마지막 문자열 순으로 정렬하도록 지정

a = ['cde', 'cfc', 'abc']

def fn(s):
    return s[0], s[-1] # s[0]이 첫 번째 기준, s[-1]이 두 번째 기준

print(sorted(a, key=fn)) # ['abc', 'cfc', 'cde']

# 만약 그냥 sorted()로 처리했다면 c가 동일하고 따라서 그 다음 문자열인
# d, f를 비교해 순서대로인 'abc', 'cde' , 'cfc' 순서로 출력될 것
# 그러나 여기서 두 번째 키로 마지막 문자열을 보게 했기 대문에
# e와 c를 비교해서 ['abc', 'cfc', 'cde'] 순으로 출력됨
 
# 다음과 같이 람다를 이용하면 함수를 별도로 정의하지 않고 한 줄로 처리도 가능
# 람다 표현식으로
a = ['cde', 'cf', 'abc']
print(sorted(a, key=lambda s: (s[0], s[-1])))