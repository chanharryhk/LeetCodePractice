class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 and n == 0:
            return 1
        if m == 0 or n == 0:
            return 0
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for y in range(1, m):
            for x in range(1, n):
                dp[y][x] = dp[y-1][x] + dp[y][x-1]
        return dp[-1][-1]
        # [1,1,1,1,1,1,1]
        # [1,2,3,4,5,6,7]      
        # [1,3,6,10,15,21,28]        