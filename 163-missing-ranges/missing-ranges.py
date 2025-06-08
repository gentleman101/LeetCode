class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        result = []

        # Check if the given list is empty
        if not nums:
            result.append([lower, upper])
            return result
        # Check for missing numbers before the first element of the given list
        if nums[0] > lower:
            result.append([lower, nums[0]-1])
        # Check for missing numbers between elements of the given list
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 1:
                result.append([nums[i-1]+1, nums[i]-1])
        # Check for missing numbers after the last element of the given list
        if nums[-1] < upper:
            result.append([nums[-1]+1, upper])
        return result
