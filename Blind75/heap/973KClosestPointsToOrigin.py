class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distances = []
        heapq.heapify(distances)
        for pos, e in enumerate(points):
            dist = math.sqrt(e[0]**2 + e[1]**2)
            heapq.heappush(distances, (dist, pos))
        
        ans = []
        for i in range(K):
            temp = heapq.heappop(distances)
            ans.append(points[temp[1]])
        
        return ans