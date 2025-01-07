class Solution:
    def maxDepth(self, s: str) -> int:

        openCounter = 0
        maxCounter = 0
        for char in s:
            if char==')':
                openCounter-=1
            elif char=='(':
                openCounter+=1
            maxCounter = max(maxCounter,openCounter)
                

        return maxCounter