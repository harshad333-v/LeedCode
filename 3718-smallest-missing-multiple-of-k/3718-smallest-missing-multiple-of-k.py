class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        return next(x for i in count(1) if (x:=k*i) not in set(nums))
