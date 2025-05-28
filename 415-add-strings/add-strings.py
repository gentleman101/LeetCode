class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        res = ""
        
        while i >= 0 or j >= 0:
            temp_sum = carry
            if i >= 0:
                temp_sum += int(num1[i])
                i -= 1
            if j >= 0:
                temp_sum += int(num2[j])
                j -= 1

            res = str(temp_sum % 10) + res
            carry = temp_sum // 10
        
        return str(carry) + res if carry else res
