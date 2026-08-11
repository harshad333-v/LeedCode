class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        result = []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = n - 1
            reqSum = 0 - nums[i]

            while l < r:
                currentSum = nums[l] + nums[r]

                if currentSum == reqSum:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif currentSum < reqSum:
                    l += 1
                else:
                    r -= 1

        return result
