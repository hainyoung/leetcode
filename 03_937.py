class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letters = []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
                
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
                
        return letters + digits
        

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letters = []
        for log in logs:
            if log.split()[1].isdigt():
                digits.append(log) # 숫자인 로그는 digits에 append
            else:
                letters.append(log) # 숫자가 아닐 경우엔 letters에 append
        
        # 식별자는 순서에 영향을 끼치지 않지만,
        # 문자가 동일할 경우 식별자 순으로 한다'는 조건에 맞추기 위해 다음의 코드 작성
        # letters 재정렬
        
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0])) # [1:] 문자를 우선, 다음엔 식별자 기준 정렬

        return letters + digits