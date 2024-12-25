class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0

        for j in range(len(nums)):
            if nums[i]==0 and nums[j]!=0:
                nums[i] = nums[j]
                nums[j] = 0
                i+=1

            elif nums[i]!=0:
                i+=1

