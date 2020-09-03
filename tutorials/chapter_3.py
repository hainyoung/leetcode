# p.73 Python

# 인덴트
# 네이밍 컨벤션 : snake_case

# list comprehension, 리스트 컴프리헨션
# 파이썬은 map, filter와 같은 함수형 Functional 기능을 지원하며 
# 다음과 같은 람다 표현식 Lambda Expression도 지원

print(list(map(lambda x: x+10, [1, 2, 3])))
# [11, 12, 13]

# 리스트 컴프리헨션은 훨씬 더 유용한 기능
# 기존 리스트를 기반으로 새로운 리스트를 만들어내는 구문! 
# 파이썬의 대표적 특징

# 리스트 컴프리헨션은 다방면에서 유용하게 활용, 무엇보다 람다 표현식에 map이나 filter를 섞어 사용하는 것에 비해
# 가독성이 훨씬 높다

# 아래는 홀수인 경우 2를 곱해 출력하라는 리스트 컴프리헨션 코드
print([n*2 for n in range(1, 10+1) if n % 2 == 1])
# [2, 6, 10, 14, 18]

# 만약 리스트 컴프리헨션을 사용하지 않는다면?
a = []

for i in range(1, 10+1):
    if i % 2 == 1:
        a.append(i * 2)

print(a) # [2, 6, 10, 14, 18]

# 위와 같이 길게 풀어서 작성해야 한다
# 풀어서 작성한 코드는 리스트 컴프리헨션에 비해 훨씬 더 길어지고 x라는 별도의 리스트 변수도 필요해짐
# 라인 수가 많이 증가함

# 리스트 컴프리헨션이라고 해서 반드시 리스트만 되는 것은 아니다
# 딕셔너리도 가능함!

# aa = {}
# for key, value in original.items():
#     a[key] = value

# 위의 코드는 아래와 같이 처리 가능
# aa = {key: value for key, value in original.items()}

# 한 줄로 간결하게 작성할 수 있는 리스트 컴프리헨션은 가독성은 좋은 편
# but, 무리하게 복잡하게 작성하면 가독성 떨어짐
# 적절히 사용!, 대체로 표현식은 2개를 넘지 않아야 함

# 제너레이터
# 제너레이터, Generator는 루프의 반복, iteration 동작을 제어할 수 있는 루틴 형태를 말한다
# 예를 들어 임의의 조건으로 숫자 1억 개를 만들어내어 계산하는 프로그램을 작성한다고 가정
# 이 경우 제너레이터가 없다면 메모리 어딘가에 만들어낸 숫자 1억 개를 보관하고 있어야 한다
# 그러나 제너레이터를 이용하면, 단순히 제너레이터만 생성해두고 필요할 때 언제든 숫자를 만들어낼 수 있다
# 만약 1억개 중 100개 정도만 쓰인다면 차이는 더욱 클 것
# 이 때 yield 구문을 사용하면 제너레이터를 리턴할 수 있다
# 기존의 함수는 return 구문을 맞닥뜨리면 값을 리턴하고 모든 함수의 동작을 종료한다
# 그러나 yield는 제너레이터가 여기까지 실행 중이던 값을 내보낸다는(단어의 사전적 의미처럼 '양보하다') 의미로,
# 중간값을 리턴한 다음 함수는 종료되지 않고 계속해서 맨 끝에 도달할 때까지 실행된다
# 물론 아래의 코드처럼 while Ture 구문은 종료 조건이 없으므로 계속해서 값을 내보낼 수 있다


'''
def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n

# 이 함수의 경우 리턴 값은 다음과 같이 제너레이터가 된다
print(get_natural_number())
# <generator object get_natural_number at 0x00000188353B2A48>


# 만약 다음 값을 생성하려면 next()로 추출하면 된다
# 예를 들어 100개의 값을 생성하고 싶다면 다음과 같이 100번 동안 next()를 수행하면 된다

g = get_natural_number()
for _ in range(0, 100):
    print(next(g))
'''


# 제너레이터는 다음과 같이 여러 타입의 값을 하나의 함수에서 생성하는 것도 가능
def generator():
    yield 1
    yield 'string'
    yield True

gen = generator()
print(gen) # <generator object generator at 0x0000020EF186E2C8>

print(next(gen)) # 1
print(next(gen)) # string
print(next(gen)) # True



# range
# 제너레이터의 방식을 활용하는 대표적인 함수로 range()가 있다
# 주로 for문에서 쓰이는 range() 함수의 쓰임은 다음과 같다

print(list(range(5))) # [0, 1, 2, 3, 4]

print(range(5)) # range(0, 5)

print(type(range(5))) # <class 'range'>

for i in range(5):
    print(i, end = ' ') # 0 1 2 3 4

print()

# 이 코드에서 range()는 range 클래스를 리턴하고,
# for문에서 사용할 경우, 내부적으로는 제너레이터의 next()를 호출하듯 매번 다음 숫자를 생성해낸다

# 만약, 생성할 숫자가 100만개쯤 된다면?
# 메모리에서 적지 않은 공간을 차지할 것이고 생성 시간도 오래 걸릴 것
# 그러나 제너레이터를 리턴하듯 range 클래스만 리턴하면 그렇지 않다
# 생성 조건만 정해두고 나중에 필요할 때 생성해서 꺼내 쓸 수 있다
# 다음은 숫자 100만개를 생성하는 2가지 방법

'''
# (1)
a = [n for n in range(1000000)]
b = range(1000000)

print(len(a)) # 1000000
print(len(b)) # 1000000
print(len(a)==len(b)) # True

# 그러나, a에는 이미 생성된 값이 담겨 있고, b는 생성해야 한다는 조건만 존재한다
# print(a)
print(type(a)) # <class 'list'>
print()
print(b) # range(0, 1000000)
print(type(b)) # <class 'range'>

print()
# a, b 사이의 메모리 점유율을 비교해보자
# range 클래스를 리턴하는 방식의 장점이 쉽게 와 닿을 것!

import sys
print("a의 방식 :", sys.getsizeof(a)) # 8697464
print("b의 방식 :", sys.getsizeof(b)) # 48

# 똑같이 숫자 100만 개를 갖고 있으나 range 클래스를 이용하는 b 변수의 메모리 점유율이 훨씬 작다
# 100만개가 아니라 1억 개라도 b 변수의 메모리 점유율은 동일하다
# why? 
# 생성 조건만 보관하고 있기 때문!
# 게다가 미리 생성하지 않은 값은 인덱스에 접근이 안 될거라고 생각할 수 있으나, 
# 인덱스로 접근 시에는 바로 생성하도록 구현되어 있기 때문에 
# 다음과 같이 리스트와 거의 동일한 느낌으로 불편 없이 사용할 수 있다
 
print(b[999]) # 999
'''


# enumerate
# enumerate()는 '열거하다'는 뜻의 함수로, 순서가 있는 자료형(list, set, tuple 등)을 인덱스를 포함한
# enumerate 객체로 리턴한다

enu = [1, 2, 3, 2, 45, 2, 5]
print(enu) # [1, 2, 3, 2, 45, 2, 5]
  
print(enumerate(enu)) # <enumerate object at 0x000001724B2255E8>

print(list(enumerate(enu))) # [(0, 1), (1, 2), (2, 3), (3, 2), (4, 45), (5, 2), (6, 5)]

# 이처럼 list()로 결과를 추출할 수 있다
# 인덱스를 자동으로 부여해주기 때문에 편리하게 활용 가능!

# 그렇다면, aaa = ['a1', 'b2', 'c3']가 있을 때, 이 리스트의 인덱스와 값을 함께 출력하려면 어떻게?

aaa = ['a1', 'b2', 'c3']
for i in range(len(aaa)):
    print(i, aaa[i])

# 0 a1
# 1 b2
# 2 c3
# 위와 같은 코드 형태를 생각할 것, 그러나 값을 가져오기 위해 불필요한 a[i] 조회 작업과 전체 길이를 조회하여 루프를 처리하는 형태 깔끔 X
# 굳이 range 사용 않고 아래와 같이 구현 가능

i = 0
for v in aaa:
    print(i, v)
    i += 1

# 0 a1
# 1 b2
# 2 c3    

# 값은 깔끔하게 처리 but 이 경우 인덱스를 위한 변수를 별도로 관리하는 형태, 깔끔 X
# 가장 깔끔한 방법은? enumerate() 활용!

for i, v in enumerate(aaa):
    print(i, v)

# 0 a1 # i : index, v : value
# 1 b2
# 2 c3

# // 나눗셈 연산자
# 5//3 == int(5/3)
# // : 몫, quotient 을 구하는 연산
# 나머지, remainder를 구하는 모듈로 연산자는 %

# 몫과 나머지를 동시에 구하려면 divmod() 함수 이용!
test = divmod(5, 3)
print(test) # (1, 2)

# print
# 코딩 테스트 문제 풀이 과정에서 디버깅을 할 때 가장 자주 쓰는 명령 : print()
# 대부분 코딩 테스트 플랫폼에서는 적어도 print()를 통해 stdout 출력결과를 부여주어 디버깅 용도로 활용할 수 있게 지원함
# 하지만 정답 제출시에는 print() 조차 보여주지 않는 경우가 있으니 유의!
# 실무에서는 이처럼 print()를 활용하는 디버깅 방법은 추천하지 않는다
# 하지만 코딩 테스트 시에는 디버거를 사용하거나 TDD방식으로 접근하기도 어렵기 때문에,
# 사실상 print()가 디버깅을 위해 제공되는 유일한 기능
# 이를 좀 더 유용하게 활용할 수 있는 방법?
# 가장 쉽게 값을 출력하는 방법은 콤마 , 로 구분하는 것
# 이 경우 한 칸 공백이디폴트로 설정되어 있으며, 그대로 출력하면 띄어쓰기로 값을 구분해준다.

print('A1', 'B2') # A1 B2

# sep 파라미터로 구분자를 콤마 , 로 지정해 줄 수도 있다
print('A1', 'B2', sep=',') # A1,B2

# print() 함수는 항상 줄바꿈을 하기 때문에 긴 루프의 값을 반복적으로 출력하면 디버깅 하기가 어려운데
# 이 경우 다음과 같이 end 파라미터를 공백으로 처리하여 줄바꿈을 하지 않도록 제한할 수 있다

print('aa', end=' ')
print('bb')
# aa bb

# 리스트를 출력할 때는 join()으로 묶어서 처리
aaa = ['A', 'B']
print(' '.join(aaa)) # A B

# 다음과 같이 idx와 fruit이 정의되어 있을 때
idx = 1
fruit = 'Apple'
# idx 값에 1을 더해서 fruit와 함께 출력하는 방법?
print('{0}: {1}'.format(idx+1, fruit)) # 2: Apple

# index 생략도 가능
print('{}: {}'.format(idx+1, fruit)) # 2: Apple

# f-string
print(f'{idx+1}: {fruit}') # 2: Apple
# 기존의 %를 사용하거나 .format을 부여하는 방식에 비해 훨씬 간결, 직관적, 속도도 빠름
# f-string은 3.6+에서만 지원!

# pass
# 코딩을 하다 보면 일단 코드의 전체 골격을 잡아 놓고 
# 내부에서 처리할 내용은 차근차근 생각하며 만들겠다는 의도로 다음과 같이 코딩하는 경우도 있다

#
from dataclasses import dataclass
# @dataclasses
# class MyClass(object):
#     def method_a(self):

#     def method_b(self):
#         print('Method B')

# c =MyClass()

# 위를 실행하면 아래의 오류 발생
'''
    def method_b(self):
          ^
IndentationError: expected an indented block
'''
# 이 문제는 method_a()가 아무런 처리를 하지 않았기 때문에 엉뚱하게 method_b()에서 오류가 발생한 것
# 필요한 오류이긴 하지만 한참 개발을 하던 중에 이런 오류를 맞닥뜨리게 되면 생각보다 처리하기가 번거롭다
# pass는 이런 오류를 막는 역할을 한다
# 다음과 같이 pass를 method_a()에 삽입해 간단히 처리할 수 있다

@dataclass
class MyClass(object):
    def method_a(self):
        # 여기에 pass 추가
        pass
    def method_b(self):
        print('Method B')

c = MyClass()
print(c.method_b())
'''
Method B
None
'''

# 파이썬에서 pass는 Null Operation 널 연산으로 아무것도 하지 않는 기능이 있다
# 이처럼 아무 역할을 하지 않는 pass를 지정하면 앞서 발생한 인덴트 오류 같은 불필요한 오류를 방지할 수 있다
# 이렇게 pass는 먼저 mockup 인터페이스부터 구현한 다음 추후 구현을 진행할 수 있게 한다
# 온라인 코딩 테스트에서 아주 유용

# try 
# except : Exception
# tracebak.print_exc()


# locals
# locals()는 로컬 심볼 테이블 딕셔너리를 가져오는 메소드로 업데이트 또한 가능하다
# 여기서는 딕셔너리를 가져오는 부분에 집중해 살펴보자면,
# 우선 로컬에 선언된 모든 변수를 조회할 수 있는 강력한 명령이므로 디버깅에 많은 도움이 된다
# 특히 로컬 스코프에 제한해 정보를 조회할 수 있기 때문에, 클래스의 특정 메소드 내부에서나 함수 내부의 로컬 정보를 조회해
# 잘못 선언한 부분이 없는지 확인하는 용도로 활용할 수 있다
# 변수명을 일일이 찾아낼 필요 없이 로컬 스코프에 정의된 모든 변수를 출력하기 때문에 편리하다
# 리트코드 문제 풀이 중에도 코드 내부에 출력해 활용할 수 있다

import pprint
pprint.pprint(locals())

'''
{'MyClass': <class '__main__.MyClass'>,
 '__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 '__cached__': None,
 '__doc__': None,
 '__file__': 'd:\\leetcode\\tutorials\\chapter_3.py',
 '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x00000165EA4CEB08>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'aaa': ['A', 'B'],
 'c': MyClass(),
 'dataclass': <function dataclass at 0x00000165EC403828>,
 'enu': [1, 2, 3, 2, 45, 2, 5],
 'fruit': 'Apple',
 'gen': <generator object generator at 0x00000165EA4F2A48>,
 'generator': <function generator at 0x00000165EA55D798>,
 'i': 2,
 'idx': 1,
 'pprint': <module 'pprint' from 'C:\\Users\\inyoung\\anaconda3\\lib\\pprint.py'>,
 'test': (1, 2),
 'v': 'c3'}
'''

# 파이썬 코딩스타일

# - snake case
# - 변수명도 의미를 담아서
# - 간단한 주석 부여(영어로 달아서 제출하면 더 프로페셔널 ㅋㅋ)
# 최소한 자연스럽게 영어로 주석을 읽고 쓰는 데 아무런 부담이 없을 정도로 익숙해져야 한다

# - 리스트 컴프리헨션
# 역할별로 줄을 구분하면 가독성 높아진다
import re

str1 = ['helloworld']
str1s = [
    str1[i:i + 2].lower() for i in range(len(str1) - 1)
    if re.findall('[a-z]{2}', str1[i:i + 2].lower())
]

# 풀어 쓰면
str1s = []
for i in range(len(str1) - 1):
    if re.finidall('[a-z]{2}', str1[i:i + 2].lower()):
        str1s.append(str1[i:i + 2].lower())

# 가독성을 위해서는 위도 나쁘지 않다
# 코드를 읽는 방향이 위에서 아래까지 차례대로 정방향이기 때문에 훨씬 이해하기 쉽다
# 짧게 쓰는 것을 고집할 필요 없음
# 리스트 컴프리헨션은 대체로 표현식이 1개를 넘지 않도록!

# Google's Python Style Guide
# 함수의 기본 값으로 가변 객체(Mutable Object)를 사용하지 않아야 한다
# 함수가 객체를 수정하면(리스트에 아이템을 추가한다든지 등) 기본값이 변경되기 때문
# 따라서 다음과 같이 기본값으로 []나 {}를 사용하는 것은 지양!

# Bad Case
# def foo(a, b=[]):
# def foo(a, b:Mapping={})

# Good Case : 불변객체(Immutable Object) 사용
# None을 명시적으로 할당!
def foo_1(a, b=None):
    if b is None:
        b = []


# def foo_2(a, b:Optional[Sequence] = None):
    # if b is None:
        # b = []

# True, False를 판별할 때는 암시적(Implicit)인 방법을 사용하는 편이 간결, 가독성 높음
# 즉, 굳이 False임을 if foo !=[]: 같은 형태로 판별할 필요가 없다
# if foo:로 충분하다

# Good Case

# (1)
# users = []

# if not users:
#     print('no users')

# (2)
# foo = 0
# if foo == 0:
#     self.handle_zero()

# (3)
# i = 10

# if i % 10 == 0:
#    self.handle_mutiple_of_ten()

# # Bad Case
# if len(users) == 0:
#     print('no users')

# if foo is not None and not foo:
#     self.handle_zero()

# if not i % 10:
#     self.handle_multiple_of_ten()

# len(users) == 0 은 길이가 없다는 말 == 값이 없다는 뜻
# (1)과 같이 not users로 충분다

# 정수를 처리할 때는 암시적으로 거짓 여부를 판별하기보다 (2)와 같이 비교 대상이 되는 정수값을 직접 비교하는 편이 덜 위험

# (3)과 같이 i % 10 == 0 으로 명시적으로 explicitly 값을 비교하는 편이 좋다

# 최대 줄 길이는 80자로 제한(암묵적 약속)

import this
'''
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''