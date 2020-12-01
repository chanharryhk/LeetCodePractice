class Solution:
    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0
        m = int(sqrt(n))
        squares = [i**2 for i in range(1,m+1)]
        # [1,4,9]
        dp = [n+1 for _ in range(n+1)]
        dp[0] = 0
        dp[1] = 1         
        for i in range(2, n+1):
            for square in squares:
                if square <= i:
                    dp[i] = min(dp[i-square]+1, dp[i])
        return dp[-1]
            
        