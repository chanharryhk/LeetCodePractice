class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # [0,0,0],
        # [0,1,0],
        # [0,0,0]
        # dp         
        # [1,1,1],
        # [1,0,1],
        # [1,1,2],
        if not obstacleGrid:
            return 0
        
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])        
        
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        
        for y in range(rows):
            if obstacleGrid[y][0] == 0:
                dp[y][0] = 1
            elif obstacleGrid[y][0] == 1:
                break
        
        for x in range(cols):
            if obstacleGrid[0][x] == 0:
                dp[0][x] = 1
            elif obstacleGrid[0][x] == 1:
                break
                
                
        for y in range(1, rows):
             for x in range(1, cols):
                if obstacleGrid[y][x] == 0:
                     dp[y][x] += dp[y-1][x] + dp[y][x-1] 
                else:
                     continue                       
        
        return dp[-1][-1]