class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        unique_chars = set()

        for right in range(len(s)):
            # If character is already in the set, shrink the window from the left
            while s[right] in unique_chars:
                unique_chars.remove(s[left])
                left += 1

            # Add the current character to the set
            unique_chars.add(s[right])

            # Update the maximum length
            max_length = max(max_length, right - left + 1)

        return max_length
