class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        hashmap = {}
        max_freq = 0
        max_length = 0
        for r in range(len(s)):
            if s[r] in hashmap:
                hashmap[s[r]]+=1
            else:
                hashmap[s[r]] = 1
                 
            max_freq = max(hashmap[s[r]],max_freq)
            if (r-l+1)-max_freq>k:
                hashmap[s[l]]-=1
                l+=1
            max_length = max(max_length,r-l+1)
        return max_length



            





        