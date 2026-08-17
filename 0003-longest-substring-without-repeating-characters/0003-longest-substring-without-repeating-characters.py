class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, max_len = 0,0
        count ={}
        for right, ch in enumerate(s):
            if ch in count and count[ch]>=left:
                left = count[ch] +1
            count[ch] = right
            max_len = max(max_len,right-left+1)
        return max_len
        