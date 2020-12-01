class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = days[-1]        
        dp = [costs[-1] for _ in range(days[-1]+1)]
        dp[0] = 0        
        # [1,4,6,7,8,20]
        # [21,21,21,21,21,21,21]       
        for i in range(1, len(dp)):
            # Only buying tickets on days that we care about            
            if i in days:
                dp[i] = min(dp[max(i-1,0)]+costs[0], dp[max(i-7,0)]+costs[1], dp[max(i-30,0)]+costs[2])
            # If it is not on a day that we care about then we the minimum remains previous             
            else:
                dp[i] = dp[i-1]
        print(dp)
        return dp[-1]
        # [0, 2, 4, 6, 7, 7, 7, 7, 9, 11, 13, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15]
        # [0, 2, 2, 2, 4, 4, 6, 7, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 11]
         