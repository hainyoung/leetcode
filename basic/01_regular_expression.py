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
print(m) # None

p = re.compile('a.b', re.DOTALL) 
m = p.match('a\nb')
print(m) # <re.Match object; span=(0, 3), match='a\nb'>
# DOTALL : Dot문자(.)가 줄바꿈 문자도 포함하도록 만드는 옵션
# re.DOTALL == re.S (약어)

# IGNORECASE, I
p = re.compile('[a-z]')
print(p.match('python')) # <re.Match object; span=(0, 1), match='p'>
print(p.match('Python')) # None
print(p.match('PYTHON')) # None

p = re.compile('[a-z]', re.I)
print(p.match('python')) # <re.Match object; span=(0, 1), match='P'>
print(p.match('Python')) # <re.Match object; span=(0, 1), match='P'>
print(p.match('PYTHON')) # <re.Match object; span=(0, 1), match='P'>

# MULTILINE, M
p = re.compile("^python\s\w+") 
# ^ : 맨 처음 을 의미
# \s : 공백 을 의미
# \w : 알파벳, 숫자, _ 중의 한 문자 를 의미
data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data)) # ['python one']

p = re.compile("^python\s\w+", re.M)

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data)) # ['python one', 'python two', 'python three']

# VERBOSE




# backslash 문제
# /section 표현식을 찾아야 할 때
# p = re.compile('\section') 이렇게 해 버리면 \s는 공백을 나타내므로 공백ection을 찾으려고 함
# 따라서 backslash임을 알려줘야하는데 
# 파이썬에서 \을 나타내려면 \\ 이렇게 2번 써 줘야함 == \section
# backslash 2개를 쓰고 싶다면? \\\\ 총 4개를 써야 함 
# 너무 복잡 - 'r'로 해결 가능
# p = re.compile('\\\\secion') == p = re.compile(r'\\section')
# 여기서 r : row! row string 임을 알려준다
# backslash는 진짜 backslash, \s 공백 나타내는 게 아니다! 임을 알려줌


# 메타문자
# 메타문자 | (프로그래밍에선 or을 의미)
import re
p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m) # <re.Match object; span=(0, 4), match='Crow'>

# 메타문자 ^
# compile 필요없이 바로 이렇게도 쓸 수 있다
print(re.search('^Life', 'Life is too short')) # <re.Match object; span=(0, 4), match='Life'>
print(re.search('^Life', 'My Life')) # None
# ^ : 맨 처음에 나오는지를 따짐

# 메타문자 $
print(re.search('Life$', 'Life is too short')) # None
print(re.search('Life$', 'My Life')) # <re.Match object; span=(3, 7), match='Life'> 
# $ : 맨 끝에 나오는지를 따짐

# 메타문자 \b
# \b : 공백을 나타내는 메타문자
p = re.compile(r'\bclass\b')
print(p.search('no class at all')) # <re.Match object; span=(3, 8), match='class'>
print(p.search('the declassified algorithm')) # None
print(p.search('one subclass is')) # None
# 공백 class 공백 <-을 찾아냄


# 그루핑 ()
# p = re.compile('ABC+') -> C만 반복됨, ABC 반복 부분을 찾고 싶다면?
p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m) # <re.Match object; span=(0, 9), match='ABCABCABC'>
print(m.group()) # ABCABCABC

# 그루핑 활용
p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d")
m = p.search("park 010-1234-1234")
print(m.group(1)) # park # (1) == \w+, 문자반복

p = re.compile(r'(\b\w+)\s+\1') # \1 : 앞에 해당 되는 것이 한 번 더 반복되는 것
print(p.search('Paris in the the pring').group()) # the the

# 그루핑 된 문자열에 이름 붙이기 : ?P<name>
p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group("name")) # park

p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
m = p.search('Paris in the the spring')
print(m.group()) # the the

# 전방탐색 : 긍정형 (?=)
p = re.compile(".+:") # :을 만날때까지만 매칭
m = p.search("http://google.com")
print(m.group()) # http:

# : 전까지만 매칭하고 싶다? ?= 을 사용
p = re.compile(".+(?=:)") 
m = p.search("http://google.com")
print(m.group()) # http
# 검색조건에는 포함되나, 결과에는 포함되지 않음

# 전방탐색: 부정형(?!)
p = re.compile(".*[.](?!bat$).*$", re.M)
l = p.findall("""
autoexec.exe
autoexec.bat
autoexec.jpg
""")
print(l) # ['autoexec.exe', 'autoexec.jpg']
# ".* 문자열이 있고 [.] 뒤에 . 이 있는데 (?!bat$).*$ 확장자명이 bat이 아닌 것"  

# 문자열 바꾸기 sub
p = re.compile('(blue|white|red)') 
print(p.sub('colour', 'blue socks and red shoes'))
# colour socks and colour shoes

# Greedy vs Non-Greedy
s = '<html><head><title>Title</title>'
# print(re.match('<.*>', s).group()) # Greedy
# <html><head><title>Title</title>
# 가장 끝 꺽쇠를 한 묶음으로 보고 <>안에  html><head><title>Title</title을 다 가져옴

print(re.match('<.*?>', s).group()) # Non-Greedy
# <html>
# ?를 써주면 매칭되는 패턴이 있을 때 최소한으로 반복한다
# 첫 < 안에 html하고 > 으로 닫힘, 딱 한 번 충족되는 것으로 출력
