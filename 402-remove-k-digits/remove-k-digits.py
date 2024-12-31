class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for n in num:
            while stack and k > 0 and n < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(n)
        
        # Handle remaining removals
        stack = stack[:-k] if k > 0 else stack
        
        # Convert to string and handle leading zeros
        result = ''.join(stack).lstrip('0')
        return result if result else "0"
