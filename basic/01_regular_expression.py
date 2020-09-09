# regular expression : 정규표현식

# 복잡한 문자열을 처리할 때 사용하는 기법, 모든 언어 공통!

# 정규표현식은 왜 필요한가?
# part 800905-1049118
# kim 700905-1059119
# 뒷자리를 별표를 하고 싶다?
# 일반적으로 한다면,,,
# 리스트에서 하나하나씩 돌면서 분리하고 인덱싱, 조건문 등 사용 -> 복잡, 코드가 길어짐

# 정규표현식으로 해결하면 단 두 줄이면 가능

import re

data = """
park 800905-1049118
kim 700905-1059119
"""

res = re.compile("(\d{6})[-]\d{7}")
print(res.sub("\g<1>-********", data))
# park 800905-********
# kim 700905-********

# 정규표현식은,,,
# 문자열의 규칙을 찾아서 어떤 것과 일치하는 것을 무엇으로 바꾸는 작업 시에 사용
# 이 문자가 어떤 규칙에 매치가 되는지 검사하는 여러 수식들이 있음

# 문자 클래스
# [abc]
# [] 사이의 문자들과 매치
# "a"는 정규식과 일치하는 문자인 "a"가 있으므로 매치
# "before"는 정규식과 일치하는 문자인 "b"가 있으므로 매치
# "dude"는 정규식과 일치하는 문자인 a, b, c 중 어느 하나도 포함 X, 따라서 매치 X
# 하이픈을 사용하여 From-To로 표현이 가능
# ex) [a-c] = [abc], [0-5] = [012345]

# Dot(.)
# a.b # . : 모든 문자를 의미!!!! (git add . 생각)
# 줄바꿈(\n)을 제외한 모든 문자와 매치
# "aab"는 가운데 문자 "a"가 모든 문자를 의미하는 '.'과 일치하므로 정규식과 매치
# "a0b"는 가운데 문자 "0"이 모든 문자를 의미하는 '.'과 일치하므로 정규식과 매치
# "abc"는 "a"문자와 "b"문자 사이에 어떤 문자라도 하나는 있어야하는 이 정규식과 일치하지 않으므로 매치 X

# 반복(*)
# ca*t # * : 앞의 문자가 여러번 반복되는 표현
# "ct"는 "a"가 0번 반복되어 매치(특이하게도 0번 반복되는 것도 매치가 된다!)
# "cat"는 "a"가 0번 이상 반복되어 매치(1번 반복)
# "caaat"는 "a"가 0번 이상 반복되어 매치(3번 반복)

# 반복(+)
# ca+t 
# "ct"는 "a"가 0번 반복되어 매치 X # * 와의 차이점!!
# "cat"는 "a"가 1번 반복되어 매치(1번 반복)
# "caaat"는 "a"가 1번 이상 반복되어 매치(3번 반복)

# 반복({m,n}, ?)
# ca{2}t
# "cat"는 "a"가 1번만 반복되어 매치되지 않음
# "caat"는 "a"가 2번 반복되어 매치 -> 이것만 유일하게 일치되는 것!

# ca{2, 5}t
# "cat"는 "a"가 1번만 반복되어 매치X
# "caat"는 "a"가 2번 반복되어 매치
# "caaaaat"는 "a"가 5번 반복되어 매치

# 반복({m,n}, ?)
# ab?c # b가 0회 혹은 1회!!
# "abc"는 "b"가 1번 사용되어 매치
# "ac"는 "b"가 0번 사용되어 매치
# ? == {0, 1}과 같은 표현

# 파이썬에서 정규 표현식을 지원하는 모듈 : re
# 사용예시
# import re
# p = re.compile("ab*")

# re.compile 해서 정규표현식을 넣어주면 패턴 객체라고 해서 p 라는 객체가 생성
# 이걸 이용해서 우리가 원하는 문자열과 비교 가능
# 패턴 객체 이용 방법 4가지 : Match, Search, Findall, Finditer


# Match
import re
p = re.compile('[a-z]+')
m = p.match('python')
# m = p.match('3 python')

print(m) 
# <re.Match object; span=(0, 6), match='python'>
# None

p = re.compile('[a-z]+')
s = p.search('python')
# s = p.search('3 python')

print(s)
# <re.Match object; span=(0, 6), match='python'>
# <re.Match object; span=(2, 8), match='python'>

p = re.compile('[a-z]+')
a = p.findall('life is too short')
print(a)
# ['life', 'is', 'too', 'short']
# 일치하는 것을 찾아서 리스트형태로 반환


p = re.compile('[a-z]+')
i = p.finditer('life is too short')
print(i)
# <callable_iterator object at 0x00000227707B0788>
for j in i:
    print(j)
# <re.Match object; span=(0, 4), match='life'>
# <re.Match object; span=(5, 7), match='is'>
# <re.Match object; span=(8, 11), match='too'>
# <re.Match object; span=(12, 17), match='short'>

#########################################################################
# Match 객체의 method
# group() : 매치된 문자열을 리턴
# start() : 매치된 문자열의 시작 위치 리턴
# end() : 매치된 문자열의 끝 위치 리턴
# span() : 매치된 문자열의 (시작, 끝)에 해당하는 튜플 리턴

p = re.compile('[a-z]+')
m = p.match('python')
print(m.group()) # python
print(m.start()) # 0
print(m.end()) # 6
print(m.span()) # (0, 6)

# compile option : DOTALL, S

# DOTALL
p = re.compile('a.b') # . : 줄바꿈을 제외한 모든 문자와 매치
m = p.match('a\nb')
print(m)