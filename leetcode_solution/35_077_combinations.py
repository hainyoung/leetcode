# 35 Combinations
# 조합


def combine_1(n: int, k: int):
    results = []
    
    def dfs(elements, start : int, k : int): #type hint
        if k == 0:
            results.append(elements[:]) # elements 복사
        
        for i in range(start, n+1):
            elements.append(i)
            dfs(elements, i + 1, k - 1)
            elements.pop()
            
    dfs([], 1, k)
    return results


# itertools module using
import itertools

def combine_2(n: int, k: int):
    return list(itertools.combinations(range(1, n+1), k))