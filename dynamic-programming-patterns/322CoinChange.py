class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1
        dp = [amount + 1 for _ in range(amount+1)]
        dp[0] = 0
        
        coins.reverse()
        
        for i in range(1, len(dp)):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i-coin] + 1, dp[i])
        if dp[-1] > amount:
            return -1
        return dp[-1]
    