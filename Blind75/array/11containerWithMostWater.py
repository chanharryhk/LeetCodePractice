class Solution:
    def maxArea(self, height: List[int]) -> int:
        h1 = 0
        h2 = len(height) - 1
        # [1,8,6,2,5,4,8,3,7]
        #         
        maxArea = 0
        while h1 != h2:
            # print(height[h1], height[h2])
            if height[h1] < height[h2]:
                maxArea = max(maxArea, (h2-h1)*(height[h1]))
                h1 += 1
            elif height[h2] <= height[h1]:
                maxArea = max(maxArea, (h2-h1)*(height[h2]))
                h2 -= 1
        return maxArea