class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, max_len = 0,0
        count ={}
        for right in range (len(s)):
            if s[right] in count:
                left = max(count[s[right]]+1,left)
            count[s[right]] = right
            max_len = max(max_len,right-left+1)
        return max_len
        