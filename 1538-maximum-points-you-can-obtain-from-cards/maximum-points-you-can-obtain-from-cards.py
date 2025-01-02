class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        leftSum = sum(cardPoints[:k])
        maxSum = leftSum
        rightSum = 0
        rightIndex = len(cardPoints)-1

        for i in range(k-1,-1,-1):
            leftSum = leftSum - cardPoints[i]
            rightSum = rightSum+cardPoints[rightIndex]
            rightIndex -=1
            maxSum = max(maxSum,leftSum+rightSum)


        return maxSum


