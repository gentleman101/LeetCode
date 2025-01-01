class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        freq_counter = []
        max_length = 0
        for r in range(len(s)):
            while s[r] in freq_counter:
                freq_counter.pop(0)
                l+=1
            freq_counter.append(s[r])
            if r-l+1>max_length:
                max_length = r-l+1
        return max_length


        