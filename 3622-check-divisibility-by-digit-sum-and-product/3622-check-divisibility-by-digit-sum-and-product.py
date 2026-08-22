class Solution:
    def checkDivisibility(self, n: int) -> bool:
        dig = [int(d) for d in str(n)]
        dig_sum = sum(dig)
        dig_prod =1
        for d in dig:
            dig_prod *=d
        total = dig_sum + dig_prod
        return n % total == 0
        