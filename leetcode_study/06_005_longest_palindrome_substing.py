class Solution:
    def longestPalindrome(self, s: str) :
        def expand(left, right): # left, right : 포인터, 단계적 확장을 위한
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ''
        for i in range(len(s)-1):
            result = max(result, expand(i, i), expand(i, i+1),
                        key = len)
        return result





'''
example = input()

def expand(left, right): # 판별 조건에 맞춰 확장할 포인터를 지정해주는 함수 정의
    while left >= 0 and right < len(example) and example[left] == example[right]: 
        # 1) left >= 0 : 두 개의 포인터 중 왼쪽으로 확장될 포인터가 index 0 까지로 제한되는 조건
        # 2) right < len(s) : 두 개의 포인터 중 오른쪽으로 확장될 포인터가 주어진 단어 길이를 넘어서면 안 되는 조건
        #                     여기서 left, right 포인터는 인덱스로 쓰이기 때문에 예를 들어 길이가 5인 단어의 마지막 포인터는 
        #                     인덱스로는 4이기 때문에 5일 수가 없다
        # 3) s[left] == s[right] : 팰린드롬을 판별할 수 있는 조건
        # 총 3가지 조건을 만족해야한다
        left -= 1 # e.g. left가 2이면 1, 0, 인덱스를 이동하면서 포인터가 확장된다
        right += 1 # right가 2이면 3, 4, 오른쪽으로 확장
    return example[left+1 : right] # while문이 false가 될 때 escape 하여 반환값을 내놓는다
                            # left는 위에서 한 번 감소하였을 때 조건에 충족 되지 않고 끝났기 때문에 다시 +1, 
                            # right는 +1 되었어도, 어차피 슬라이싱에선 끝자리 포함이 되지 않으므로 right로만 쓰면 된다

if len(example) < 2 or example == example[::-1]: # 단어의 길이가 1일때 e.g. example = "a"이면 그냥 a만 반환하면 되고, 
                                                reverse 했을 때 같은 경우엔 단어 전체가 가장 긴 팰린드롬임이 충족되므로 그냥 반환
    print(example)

# 위의 if문을 충족하지 않는 경우에는 아래의 for문에 들어간다

result = ''
for i in range(len(example)-1): # -1 해주지 않아도 정답으로 뜨긴 함
                                # 해 주는 이유를 생각해보자면
                                # 5자리수의 단어이면 range(4), i는 3까지 들어가고 두 번째 expand()에 3, 4가 들어감
                                # 만약 -1 하지 않고 5로 하면 i는 4까지 들어가고 두 번째 expand()에 4, 5가 들어감 index 5는 존재하지 않음, 
                                # 무조건 expand 조건 충족을 못하니까 따라서 여기서 미리 처리?

    result = max(result, expand(i, i), expand(i, i+1), key = len)

print(result)
'''
    
##################################################################################################################################

# Given a string s, find the longest palindromic substring in s. 
# You may assume that the maximum length of s is 1000.

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Input: "cbbd"
# Output: "bb"

def longestPalindrome(s: str):
    def expand(left: int, right: int):
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    for i in range(len(s)-1):
        result = max(result, expand(i, i), expand(i, i+1), key=len)
    return result

sent = "babad"
print(longestPalindrome(sent))


'''
class Solution:
    def longestPalindrome(self, s: str) :
        def expand(left, right): # left, right : 포인터, 단계적 확장을 위한
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ''
        for i in range(len(s)-1):
            result = max(result, expand(i, i), expand(i, i+1),
                        key = len)
        return result



'''

# review 0930
