# 2020년 06월 25일
# 10172번 : 개

# 아래 예제와 같이 개를 출력하시오.

# |\_/|
# |q p|   /}
# ( 0 )"""\
# |"^"`    |
# ||_/=\\__|

# 통과
print("|\_/|\n|q p|  /}\n( 0 )\"\"\"\\\n|\"^\"`    |\n||_/=\\\\__|\n")

# trial and error
# 4월 기초 강의, 파이썬 시간에 배운 것이 생각나서 끌어옴
fixStr = """
    여기에 이런식으로 적으면
            여기 적은 형태로
            출력되게 된다.
"""
print(fixStr)

# 출력화면
'''
    여기에 이런식으로 적으면
            여기 적은 형태로
            출력되게 된다.
'''
# 적용 
# 파이썬에서 몇 가지 특수문자는 \와 함께 입력해야 제대로 출력된다
# \ 를 표시하고 싶다면 \\
# " 를 표시하고 싶다면 \"
# '를 표시하고 싶다면 \'

dog = """
|\_/|
|q p|   /}
( 0 )\"\"\"\\
|"^"`    |
||_/=\\\\__|    
"""
print(dog)
# 이렇게 답안 제출을 했더니,,,
# 출력 화면은 문제 정답과 같은데
# '출력 형식이 잘못되었습니다' 라는 결과가 나옴
# 이런 방식이 아니라 일렬로 써 주고 개행문자를 이용해야 하는 건가 싶어서
# 한 줄로 붙이고 사이사이 개행문자를 써 주었더니 통과되었다
# dog = "|\_/|\n|q p|   /}\n( 0 )\"\"\"\\\n|\"^\"`    |\n||_/=\\\\__|\n"
# print(dog)


# "(큰 따옴표) 는 '(작은 따옴표) 사이에 넣어도 출력이 가능하다
print("======================================================")

dog = """
|\_/|
|q p|   /}
( 0 )'"''"''"'\\
|"^"`    |
||_/=\\\\__|
"""
print(dog)

# 큰따옴표를 표기하고 싶다면 print()에서 '로 묶어주면 된다

print('''|\_/|
|q p|   /}
( 0 )"""\\
|"^"`    |
||_/=\\\__|''')