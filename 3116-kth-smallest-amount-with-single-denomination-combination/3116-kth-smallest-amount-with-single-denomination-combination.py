class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def count(x):
            n = len(coins)
            ans = 0
            for mask in range(1, 1 << n):
                mult = 1
                bits = 0
                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        mult = lcm(mult, coins[i])
                        if mult > x:  
                            break
                else:
                    if mult > x:
                        continue
                    value = x // mult
                    if bits % 2 == 1:
                        ans += value
                    else:
                        ans -= value
            return ans

        
        left, right = 1, 10**18
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left
