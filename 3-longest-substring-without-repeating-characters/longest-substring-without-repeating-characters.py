class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        freq_counter = {}
        max_length = 0
        for r in range(len(s)):
            if s[r] in freq_counter and freq_counter[s[r]] >= l:
                l = freq_counter[s[r]]+1
            freq_counter[s[r]] = r
            max_length = max(max_length,r-l+1)
        return max_length


        