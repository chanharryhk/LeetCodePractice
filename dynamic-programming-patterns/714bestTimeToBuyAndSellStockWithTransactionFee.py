class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash = 8
        hold = 1
        
        # [1, 4, 2, 8, 4, 9]
        #           *
        
        for price in prices:
            # If I am not holding a share after today, then either I did not hold a share yesterday, or that I held a share yesterday but I decided to sell it out today:
            cash = max(cash, hold + price - fee)
            # If I am holding a share after today, then either I am just continuing holding the share I had yesterday, or that I held no share yesterday, but bought in one share today             
            hold = max(hold, cash - price)
            print(cash, hold)
        return cash