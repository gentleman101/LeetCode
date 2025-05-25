class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        power = abs(n)
        current = x

        while power > 0:
            if power % 2 == 1:
                res *= current
            current *= current
            power //= 2

        return res if n >= 0 else 1 / res
