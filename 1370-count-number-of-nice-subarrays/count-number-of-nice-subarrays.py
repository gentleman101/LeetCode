from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_count = {0: 1}  # To handle cases where odd_count == k
        odd_count = 0
        cnt = 0

        for num in nums:
            # Increment odd_count if the number is odd
            if num % 2 == 1:
                odd_count += 1

            # Check if there exists a prefix with odd_count - k
            if odd_count - k in prefix_count:
                cnt += prefix_count[odd_count - k]

            # Update the prefix_count for the current odd_count
            prefix_count[odd_count] = prefix_count.get(odd_count, 0) + 1

        return cnt
