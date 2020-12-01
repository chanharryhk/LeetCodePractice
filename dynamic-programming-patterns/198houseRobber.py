class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        # [0,7,9,4,10]
        # [0,7,9,11,19]
        if n <= 2:
            return max(nums)
        nums[1] = max(nums[:2])
        for i in range(2,n):
            nums[i] = max(nums[i-1], nums[i]+nums[i-2])         
        return nums[-1]         
    