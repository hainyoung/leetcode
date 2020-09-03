# 36 combination sum
# 조합의 합

def combinationSum(self, candidates: List[int], target: int):
    
    result = []
    
    def dfs(csum, index, path):
        if csum < 0:
            return
        if csum == 0:
            result.append(path) # target을 맞춘 상황?
            return
        
        for i in range(index, len(candidates)):
            dfs(csum - candidates[i], i, path + [candidates[i]])
            
    dfs(target, 0, [])
    return result
            