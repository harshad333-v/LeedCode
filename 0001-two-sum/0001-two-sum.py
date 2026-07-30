class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, v in enumerate(nums):
            comp = target - v
            if comp in seen:
                return [seen[comp], i]
            seen[v] = i
        return [] 
