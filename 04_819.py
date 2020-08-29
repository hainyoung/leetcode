class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.sub('[^\w]', ' ', paragraph).lower().split() 
        
        # re.sub : 정규 표현식
        # 단어가 아닌 것들은 모두 공백 처리, 소문자로 모두 바꿔주고, 공백을 기준으로 배열 생성
        
        words = filter(lambda x: x not in banned, words) # banned 에 속한 단어는 필터링 해주는 작업, banned에 속하지 않는 단어들만 words 변수에 넣어준다, 마지막 words는 input
        
        counter = collections.Counter(words) # collections의 Counter라는 자료구조를 사용하면 words안의 단어들의 개수를 세어 준다    # print(words)
        # print(counter) # 단어별로 몇 번 등장하는지 딕셔너리 형태로 출력
        # print(counter.most_common(1)) # 가장 많이 등장하는 단어, 등장 개수를 출력해주는 most_common() 함수를 사용
        # [('ball', 2)] 이런 식으로 나오기 때문에
        # print(counter.most_common(1)[0][0])
        # 위와 같이 위치를 지정해줘야 한다
        # ball
        
        return counter.most_common(1)[0][0]