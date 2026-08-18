class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k==1:
            freq = Counter(nums)
            candidates = [x for x in freq if freq[x]==1]
            return max(candidates) if candidates else -1

        if k==n:
            return max(nums)

        freq = Counter(nums)
        left, right = nums[0], nums[-1]

        candidates = []
        if freq[left] == 1:
            candidates.append(left)
        if freq[right] == 1:
            candidates.append(right)

        return max(candidates) if candidates else -1

        