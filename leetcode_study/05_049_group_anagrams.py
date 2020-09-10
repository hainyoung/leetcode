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