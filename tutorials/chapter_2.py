# p.056
# 루프
#  1부터 10까지 합

# C++
# int sum = 0;
# for (int i =1; i<=10;, i++){
#     sum += i;
# }

# Java
# int sum = 0;
# for (int i = 1; i <=10; i++){
#      sum += i;}

# Python
# 예시1)
add_1 = 0
for i in range(1, 10+1):
    add_1 += i

print(add_1)

# 예시2
add_2 = sum(i for i in range(1, 10+1))

print(add_2)

# 예시3
add_3 = sum(range(1, 10+1))

print(add_3)

# 제네릭 프로그래밍
# generic이란 파라미터의 타입이 나중에 지정(to be specified later)되게 해서 재활용성을 높일 수 있는 프로그래밍 스타일
# 1989년 데이비드 무저와 알렉산더 스테파노프가 고안
# C++, Java는 제네릭 프로그래밍 문법이 존재하지만
# 파이썬은 원래 동적 타이핑 Dynamic Typing 언어이기 때문에 제네릭이 필요 없다

def are_equal_1(a, b):
    return a==b

print(are_equal_1(10, 10.0))
# True

# 하지만 동적 타이핑의 장점이자 단점은 얼핏 사용하기엔 매우 편하지만 코드의 복잡도가 높아질수록 혼란을 가중시킨다는 점이다
# 타입을 아예 명시하지 않으면 가독성을 낮추고 버그 발생 확률이 높아진다
# 따라서 다음과 같이 타입을 명시할 수 있다

from typing import TypeVar

T = TypeVar('T')
U = TypeVar('U')

def are_equal_2(a: T, b: U):
    return a==b

print(are_equal_2(10, 10.0))
# True


# 배열 반복
# 각 언어별 문자열 배열(python에서는 list)을 반복하면서 element를 출력하는 코드 작성

# C++
# std::string foo[] = {"A", "B", "C"};
# for (std::string f : foo){
#     std::cout << f << std::end;
# }

# Java
# String[] foo = new String[]{"A", "B", "C"};
# for (String f : foo) {
#     System.out.println(f);
# }

# Python
foo = ['A', 'B', 'C']
for f in foo :
    print(f)


# p.061 구조체
# C에서는 구조체, Struct은 특별한 의미가 있다. 순차적으로 메모리를 할당하는 배열과 달리
# 구조체는 메모리의 어느 영역에나 어떤 크기로든 할당할 수 있는 사실상 유일한 복합 자료형이기 때문이다
# 연결 리스트를 포함해 배열을 제외한 모든 추상 자료형 ADT(Abstract Data Type, 추상 자료형이란 자료형의 연산을 정의한 것으로 실제 구현 방법은 명시하지 않는다)의
# 구현은 사실상 구조체를 한 번 이상 이용한다고 할 수 있다
# C++에서 클래스의 등장으로(원래 C++의 이름은 C with Classes였다) 이후 등장한 언어들에는 사용 빈도가 줄었지만 여전히 구조체는 널리 쓰이고 있다

# Python
from collections import namedtuple
MyStruct = namedtuple("MyStruct", "field1 field2 field3")

m = MyStruct("foo", "bar", "baz")

print(m) # MyStruct(field1='foo', field2='bar', field3='baz')

# 파이썬에는 구조체가 없을 뿐더러 클래스 또한 데이터 타입을 지정할 수 없어, 구조체와 같은 형태를 정의하려면
# namedtuple을 사용해야 했다
# 이처럼 정의해 사용하는 방법밖에 없었는데 파이썬 3.7부터 dataclass를 지원하며 @dataclass 데코레이션(Decoration, Java에서는 동일한 문법을 Annotation이라 함)으로
# 타입 힌트와 함께 활용함으로써 다음과 같이 class를 이용해 구조체 형태로 정의할 수 있다

# Python 3.7+
from dataclasses import dataclass

@dataclass
class Product:
    weight: float = None
    price: int = None

apple = Product()
apple.price = 10

print(apple) # Product(weight=None, price=10)

apple.weight = 2.5

print(apple) # Product(weight=2.5, price=10)

# p.063 클래스
# 실무에서는 거의 항상 쓰이지만 코딩 테스트에서는 클래스까지 사용할 일이 사실 드물다
# 그러나 클래스는 현대 프로그래밍 언어에서 빼놓을 수 없는 필수 기능! 

# Python
from dataclasses import dataclass

@dataclass
class Rectangle:
    width: int
    height: int
    
    def area(self):
        return self.width*self.height

rect = Rectangle(3, 4)
print(rect.area()) # 12

# self는 class Rectangle을 가리킨다
# class Rectangle의 width, height를 가져온다?

