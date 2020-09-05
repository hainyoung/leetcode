# 빅오, 자료형

# 자료형
# 파이썬 자료형 

# None : class None Type

# 숫자 
# - 정수형 : 정수(class int), 불리언(class bool)
# - 실수형(class float)

# 집합형
# - 집합(class set)

# 매핑
# - 딕셔너리(class dict)

# 시퀀스
# - 불변 : 문자열(class str), 튜플(class tuple), 바이트(class bytes)
# - 가변 : 리스트(class lit)


# 숫자
# 파이썬에서는 숫자 정수형으로 int만을 제공
# int보다 더 큰 값은 어떤 자료형에 보관? 
# 원래 파이썬은 ver2 까지 int와 long을 별도로 제공
# int는 C 스타일의 고정 정밀도(fixed-precision) 정수형이었고
# long은 임의 정밀도(arbitraray-precision)이었다
# 2.4 부터는 int가 충분하지 않으면 자동으로 long 타입으로 변경되는 구조가 됨
# C와 달리 overflow가 발생하는 일이 사라짐
# ver3 부터는 아예 int 단일형으로 통합
# int는 임의 정밀도를 지원, 더이상 파이썬에서 고정 정밀도 정수형은 지원 X

# BOOL은 엄밀히 따지자면 논리형 자료형, 파이썬에서는 내부적으로 1(True), 0(False)으로 처리되는
# int의 usb class이다
# int는 object의 하위 클래스이기도 하기 때문에 결국 다음과 같은 구조를 띤다

# object > int > bool

# 논리 자료형의 값인 True와 정수형의 값인 1을 비교해보면 다음과 같다
print(True==1) # True
print(False==0) # True

# 비교연산자 == 을 통해 확인한 결과, 논리 자료형은 내부적으로 정수값을 가지고 있음을 확인할 수 있다

# 매핑
# 매핑 Mappping 타입은 키와 자료형으로 구성된 복합 자료형
# 파이썬에서 내장된 유일한 매핑 자료형은 딕셔너리


# 집합
# 파이썬의 집합 자료형인 set은 중복된 값을 갖지 않는 자료형
# 파이썬에서 빈 집합은 다음과 같은 형태로 선언
a = set()
print(a) # set()
print(type(a)) # <class 'set'>

# 빈 집합이 아닌 값이 포함된 집합을 선언할 때는 a = {1, 2, 3} 형태로 하는데
# 집합은 딕셔너리와 동일하게 중괄호 {}를 사용하므로 유의
# 구분하는 방법?
# 딕셔너리는 key, value 형태이지만 집합은 value, 값만 선언하므로 선언 형태를 보면 타입 판단 가능
# 파이썬 컴파일러는 타입 결정을 자동으로 한다

a = {'a', 'b', 'c'}
print(type(a)) # <class 'set'>

a = {'a': 'A', 'b': 'B', 'c' : 'C'}
print(type(a)) # <class 'dict'>

# set은 입력 순서가 유지되지 않으며!!! 다음처럼 중복된 값이 있을 경우 하나의 값만 유지한다
a = {3, 2, 3, 5}
print(a) # {2, 3, 5}