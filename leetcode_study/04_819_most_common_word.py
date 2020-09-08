# 금지된 단어를 제외한 가장 흔하게 등장하는 단어 출력
# 대소문자 구분 하지 않고 구두점 또한 무시



# list comprehension, Counter 객체 사용
import collections

# 입력값에는 대소문자가 섞여 있으며 쉼표 등의 구두점이 존재
# 따라서 데이터 클렌징 data cleansing 이라 부르는 입력값에 대한 preprocessing 작업이 필요
# 더 편리하게 처리하기 위해 정규식을 쓰면 다음과 같이 처리 가능


# most_common_word
# 
# # paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# (1))
# words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
# print(words)
# (2)
# words = []
# for c in word:
#     if c not in banned:
#         words.append(c)
# print(words)
# (1) == (2) (1)처럼 간단히 표현 가능