class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l, m, r = 0, 0, len(nums) - 1

        while m <= r:  # We use m <= r to ensure we check the entire list
            if nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                l += 1
                m += 1
            elif nums[m] == 1:
                m += 1
            else:  # nums[m] == 2
                nums[m], nums[r] = nums[r], nums[m]
                r -= 1

