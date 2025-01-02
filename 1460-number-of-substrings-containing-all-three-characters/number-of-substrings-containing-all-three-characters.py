class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        hashMap = {}
        hashMap['a'] = -1
        hashMap['b'] = -1
        hashMap['c'] = -1
        cnt = 0
        for i,char in enumerate(s):
            hashMap[char] =i
            cnt+=1 + min(hashMap['a'],hashMap['b'],hashMap['c'])

        return cnt
            
        