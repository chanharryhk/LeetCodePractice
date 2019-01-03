class Solution:
    def checkPossibility(self, nums):
        biggerCount = 0
        max = 0
        if len(nums) == 1:
            return True
        for i in range(0, len(nums) - 1):
            if nums[i+1] < nums[i]:
                biggerCount += 1
        print(biggerCount)
        if biggerCount == 1 or biggerCount == 0:
            return True
        else:
            return False

test = [3,4,2,3]
x = Solution()
print(x.checkPossibility(test))