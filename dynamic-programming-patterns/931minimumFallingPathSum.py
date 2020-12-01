class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        if not A:
            return 0
        
        xMax = len(A)
        yMax = len(A[0])
        
        for y in range(1, yMax):
            for x in range(xMax):
                if x == 0:
                    A[y][x] += min(A[y-1][x], A[y-1][x+1])
                elif x == xMax-1:
                    A[y][x] += min(A[y-1][x], A[y-1][x-1])
                elif 0 < x < xMax-1:
                    A[y][x] += min(A[y-1][x], A[y-1][x+1], A[y-1][x-1])
        
        return min(A[-1])