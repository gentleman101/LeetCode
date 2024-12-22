class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Remove duplicates and sort the numbers
        sorted_nums = sorted(set(nums))
        
        max_length = 1
        current_length = 1
        
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i - 1] + 1:
                # Increment the current sequence length
                current_length += 1
                max_length = max(max_length, current_length)
            else:
                # Reset current length if the sequence is broken
                current_length = 1
        
        return max_length
