def letterCombinations(digits: str) -> List[str]:
    def dfs(index, path):
        if len(path) == len(digits):
            result.append(path)
            return
        
        for i in range(index, len(digits)):
            for j in dic[digits[i]]: # 2 에 a 하나 b 하나 c 하나 불러옴
                dfs(i + 1, path + j) # j : 문자열 a or b or c
    
    
    if not digits:
        return []
    
    dic = {"2": "abc", "3": "def", "4" : "ghi", "5" : "jkl", 
            "6": "mno", "7": "pqrs", "8":"tuv", "9" :"wxyz"}
    
    result = []
    dfs(0, "")
    
    return result
        