class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rev_row = defaultdict(int)
        for row, seat in reservedSeats:
            rev_row[row]|= 1<<(10-seat)
        family_group = (0b0111100000, 0b0000011110, 0b0001111000)
        total_families = (n - len(rev_row))*2
        for row_res in rev_row.values():
            for mask in family_group:
                if (row_res & mask)== 0:
                    row_res |= mask
                    total_families +=1
        return total_families