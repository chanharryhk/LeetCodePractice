class Solution:
    def twoSum(self, nums, target):
        # dictionary to store potential pairs
        numPair = {}
        # list to contain the answers of the indexes of the solution
        ans = []
        # iterating through all fo the numbers in the given list
        for i in range(len(nums)):
            # if the solution already exists in our dictionary
            lookUp = target - nums[i]
            if lookUp in numPair:
                # return ans
                ans = [nums.index(lookUp), i]
                print(ans)
                return ans
            else:
                # add number key pair to our dictionary
                numPair[nums[i]] = lookUp

testArr = [0,4,3,0]
# Create a new x object as a class Solution
x = Solution()
# Calling the function twoSum inside the object x
x.twoSum(testArr,0)

