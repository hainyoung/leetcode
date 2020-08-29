
from collections import defaultdict

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(type(strs)) # <class 'list'>

anagrams = defaultdict(list) 

print(type(anagrams)) # <class 'collections.defaultdict'> 

print(anagrams) # defaultdict(<class 'list'>, {})

for word in strs:
    words = sorted(word)
    print(words)
    '''
    ['a', 'e', 't']
    ['a', 'e', 't']
    ['a', 'n', 't']
    ['a', 'e', 't']
    ['a', 'n', 't']
    ['a', 'b', 't']
    '''
    anagrams[''.join]

    # anagrams['']



# https://dongdongfather.tistory.com/69
# defaultdict?
# dictionary를 만드는 dict calss의 sub class이다
# defaultdict()는 인자로 주어진 객체(default-factory)의 기본값을 dictionary의 초깃값으로 지정할 수 있다
# 숫자, 리스트, 셋 등으로 초기화 할 수 있기 때문에 여러 용도로 사용할 수 있다

# e.g.
# from collections import defaultdict # 외부함수이므로 import
# int_dict = defaultdict(int)
# print(int_dict) -> defaultdict(<class 'int'>, {}) # 디폴트값이 int인 딕셔너리
# 위와 같이 설정하면 값을 지정하지 않은 key는 0으로 지정됨
# print(int_dict['key1'])
# 0

# print(int_dict)
# decaultdict(<class 'int'>, {'key1':0})
