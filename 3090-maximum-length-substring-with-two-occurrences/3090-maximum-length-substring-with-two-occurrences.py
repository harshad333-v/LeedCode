class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left,max_len = 0,0
        count = {}
        for  right in range (len(s)):
            count[s[right]] = count.get(s[right], 0)+1
            while count[s[right]]>2:
                count[s[left]]-=1
                left += 1
            max_len = max(max_len, right - left+1)

        return max_len