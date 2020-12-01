class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxProf = 0
        # minPrice = float("inf")
        # for price in prices:
        #     maxProf = max(maxProf, price-minPrice)
        #     minPrice = min(minPrice, price)
        # return maxProf
        
        # [7,1,5,3,6,100]   
        
        maxProf = 0
        minPrice = float("inf")
        for price in prices:
            if price - minPrice > 0:
                maxProf += price-minPrice
                minPrice = price
            else:
                minPrice = min(minPrice, price)        
        return maxProf