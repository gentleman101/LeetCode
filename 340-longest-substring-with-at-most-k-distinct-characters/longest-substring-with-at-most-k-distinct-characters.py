class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        hashMap = {}
        l=0
        longest = 0

        for i,char in enumerate(s):
            hashMap[char] = hashMap.get(char,0)+1

            if len(hashMap)>k:
                 hashMap[s[l]]-=1
                 if hashMap[s[l]]==0:
                    hashMap.pop(s[l])
                 l+=1
            
            longest = max(longest,i-l+1)
        return longest