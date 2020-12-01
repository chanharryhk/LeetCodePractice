class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        
        rows = len(triangle)
        for y in range(1, rows):
            columns = len(triangle[y])
            for x in range(columns):
                if x == 0:
                    triangle[y][x] += triangle[y-1][x]
                elif x == columns - 1:
                    triangle[y][x] += triangle[y-1][x-1]
                # middle                 
                else:
                    triangle[y][x] += min(triangle[y-1][x-1], triangle[y-1][x])
        
        return min(triangle[-1])