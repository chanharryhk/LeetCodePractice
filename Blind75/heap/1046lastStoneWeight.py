class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Turns it into max heap       
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = -1 * heapq.heappop(stones)
            second = -1 * heapq.heappop(stones)                
            if first - second != 0:
                heapq.heappush(stones,  -1 * (first - second))
        
        if stones:
            return stones[0] * -1
        else:
            return 0