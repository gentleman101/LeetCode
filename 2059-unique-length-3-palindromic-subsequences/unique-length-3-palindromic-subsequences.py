class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        res = set()
        countDict = Counter(s)
        leftSet = set()
        cnt = 0

        for i in range(n):
            countDict[s[i]]-=1
            if countDict[s[i]]==0:
                countDict.pop(s[i])

            for c in leftSet:
                if c in countDict:
                    res.add((s[i],c))
            leftSet.add(s[i])

        return len(res)
        