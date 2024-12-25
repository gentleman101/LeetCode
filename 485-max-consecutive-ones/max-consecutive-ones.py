class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        length = 0
        max_length = 0
        for j in range(len(nums)):
            if nums[j]==1:
                length+=1
                max_length = max(max_length,length)

            else:
                length = 0

        return max_length


        