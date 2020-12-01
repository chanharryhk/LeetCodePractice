class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        xMax, yMax = len(grid), len(grid[0])
        for x in range(xMax):
            for y in range(yMax):
                if 0 < x and 0 < y:
                    grid[x][y] += min(grid[x-1][y],  grid[x][y-1])
                elif 0 < x:
                    grid[x][y] += grid[x-1][y]
                elif 0 < y:
                    grid[x][y] += grid[x][y-1]
        return grid[-1][-1]
