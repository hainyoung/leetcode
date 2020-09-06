

def numIslands_1(grid: List[List[str]]):
    def dfs(i, j):
        if i < 0 or i >= len(grid) or \
            j < 0 or j >= len(grid[0]) or \
            grid[i][j] != '1':
            return
        
        grid[i][j] = 0
        # i: 행을 탐색, j: 열을 탐색
        dfs(i+1, j) # 북쪽
        dfs(i -1, j) # 남쪽
        dfs(i, j+1) # 동쪽
        dfs(i, j-1) # 서쪽
        
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1': # 땅이면 탐색
                dfs(i, j)
                count +=1 
    return count



    
def numIslands(grid: List[List[str]]):
    R = len(grid)
    
    C = len(grid[0]) if len(grid) else 0
    
    
    def dfs(i, j):
        if i < 0 or i >= R or \
            j < 0 or j >= C or \
            grid[i][j] != '1':
            return
        
        grid[i][j] = 0
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            i2, j2 = i + di, j + dj
            dfs(i2, j2)
        
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1': # 땅이면 탐색
                dfs(i, j)
                count +=1 
    return count