class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return
        i = 1
        single = nums[0]
        while i != len(nums):
            if single != nums[i]:
                single = nums[i]
                i += 1
            else:
                nums.pop(i)
                
            
            
        