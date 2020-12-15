class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        ptr1, ptr2 = 0, 0
        window = 0
        ans = float("inf")
        nums.append(0)
        while ptr2 < len(nums):
            if window < s:                
                window += nums[ptr2]
                ptr2 += 1
            else:
                ans = min(ans, ptr2-ptr1)
                window -= nums[ptr1]
                ptr1 += 1
        return 0 if ans == float("inf") else ans