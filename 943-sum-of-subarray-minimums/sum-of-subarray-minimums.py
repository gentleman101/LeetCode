from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = int(1e9 + 7)
        
        # PSEE (Previous Smaller Element's index)
        pse = [-1] * len(arr)
        pse_stack = []
        for num in range(len(arr)):
            while pse_stack and arr[num] < arr[pse_stack[-1]]:
                pse_stack.pop()
            pse[num] = pse_stack[-1] if pse_stack else -1
            pse_stack.append(num)
        
        # NSE (Next Smaller Element's index)
        nse = [len(arr)] * len(arr)
        nse_stack = []
        for num in range(len(arr) - 1, -1, -1):
            while nse_stack and arr[num] <= arr[nse_stack[-1]]:
                nse_stack.pop()
            nse[num] = nse_stack[-1] if nse_stack else len(arr)
            nse_stack.append(num)
        
        # Calculate the total
        total = 0
        for i in range(len(arr)):
            left = i - pse[i]
            right = nse[i] - i
            total += (right * left * arr[i]) % mod
        
        return total % mod
