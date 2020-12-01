class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        rows = len(matrix)
        columns = len(matrix[0])
        res = 0
        dp = [[0 for _ in range(columns+1)] for _ in range(rows+1)]
        for y in range(1, rows+1):
            for x in range(1, columns+1):
                if matrix[y-1][x-1] == "1":
                    # take the minimum to see if the others make a square                     
                    dp[y][x] = min(dp[y-1][x-1], dp[y-1][x], dp[y][x-1]) + 1
                    res = max(dp[y][x], res)
        print(dp)
        return res ** 2
        # dp =     
        # [0,0,0,0,0,0]
        # [0,1,0,1,0,0]
        # [0,0,0,0,0,0]
        # [0,0,0,0,0,0]
        # [0,0,0,0,0,0]
                
        # [1, 0, 1, 1, 1],
        # [1, 0, 1, 1, 1],
        # [1, 1, 1, 1, 1],
        # [1, 0, 0, 1, 0],
        
        # [0, 0, 0, 0, 0, 0],
        # [0, 1, 0, 1, 1, 1],
        # [0, 1, 0, 1, 2, 2],
        # [0, 1, 1, 1, 2, 3],
        # [0, 1, 0, 0, 1, 0]
        
        # [1,1]
        # [1,1]
