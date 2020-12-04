class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(x,y):
            # print(x,y)
            if 0 <= x < cols and 0 <= y < rows:
                if grid[y][x] == "1":
                    grid[y][x] = "0"
                    dfs(x+1, y)
                    dfs(x-1, y)
                    dfs(x, y+1)
                    dfs(x, y-1)
            
        res = 0
        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == "1":
                    dfs(x,y)
                    res += 1
        return res
                    
                
                