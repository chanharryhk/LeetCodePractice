class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        xMax = len(grid)
        yMax = len(grid[0])
        
        islands = 0
        
        def dfs(x, y, grid):
            if x >= 0 and y >= 0 and x < xMax and y < yMax and grid[x][y] == '1':
                grid[x][y] = '0'
                dfs(x-1, y, grid)
                dfs(x+1, y, grid)
                dfs(x, y-1, grid)
                dfs(x, y+1, grid)
            
        
        for x in range(xMax):
            for y in range(yMax):
                if grid[x][y] == '1':
                    dfs(x, y, grid)
                    islands += 1
        
        return islands
                        