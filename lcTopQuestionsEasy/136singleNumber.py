class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        duplicate = nums[0]
        i = 1
        while i != n:
            if nums[i] != duplicate:
                return duplicate
            else:
                duplicate = nums[i+1]
                i += 2
        return nums[-1]
        
            
            