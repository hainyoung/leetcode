from typing import List
import re
import collections

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]):
        words = re.sub('[^\w]', ' ', paragraph).lower().split() 
        
        # re.sub : 정규 표현식
        # 정규식에서 \w는 단어 문자를 뜩하고 ^은 not을 의미한다
        # 위 정규식은 단어가 아닌 것들은 모두 공백으로 치환하는 역할을 함
        # + lower()로 소문자자로 모두 바꿔주고, 공백을 기준으로 배열 생성
        # 
        
        words = filter(lambda x: x not in banned, words) # banned 에 속한 단어는 필터링 해주는 작업, banned에 속하지 않는 단어들만 words 변수에 넣어준다, 마지막 words는 input
        
        counter = collections.Counter(words) # collections의 Counter라는 자료구조를 사용하면 words안의 단어들의 개수를 세어 준다    # print(words)
        # print(counter) # 단어별로 몇 번 등장하는지 딕셔너리 형태로 출력
        # print(counter.most_common(1)) # 가장 많이 등장하는 단어, 등장 개수를 출력해주는 most_common() 함수를 사용
        # [('ball', 2)] 이런 식으로 나오기 때문에
        # print(counter.most_common(1)[0][0])
        # 위와 같이 위치를 지정해줘야 한다
        # ball
        
        return counter.most_common(1)[0][0]

#########################################################################################################################

# 금지된 단어를 제외한 가장 흔하게 등장하는 단어 출력
# 대소문자 구분 하지 않고 구두점 또한 무시



# list comprehension, Counter 객체 사용


# 입력값에는 대소문자가 섞여 있으며 쉼표 등의 구두점이 존재
# 따라서 데이터 클렌징 data cleansing 이라 부르는 입력값에 대한 preprocessing 작업이 필요
# 더 편리하게 처리하기 위해 정규식을 쓰면 다음과 같이 처리 가능
# most_common_word
# 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
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
from typing import List
import collections
import re
def mostCommonWrod(paragraph: str, banned: List[str]):
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]

print(mostCommonWrod(paragraph, banned))

# 0928 review
