class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        for i, val in enumerate(nums):
            key = target - val
            if key in hashmap:
                return [hashmap[key],i]
            hashmap[val] = i
        