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
#
