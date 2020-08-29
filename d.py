from dataclasses import dataclass

@dataclass
class Rectangle :
    width : int
    height : int

    def area(self) :
        return self.width * self.height


rect = Rectangle(3, 4)
print(rect.area())

import collections

a = collections.defaultdict(int) # 초기값으로 0이 들어가 있기 때문에

a['A'] = 5
a['B'] = 4

print(a)

a['C'] += 1 # 초기값 세팅해주는 defaultdict 특성으로 이렇게 1을 더하는 방식으로 key, value 추가 가능하다

print(a)

