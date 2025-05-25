class Solution:
    def myPow(self, x: float, n: int) -> float:

        def recur(i):
            if i == 0:
                return 1
            half = recur(i // 2)
            if i % 2 == 0:
                return half * half
            else:
                return half * half * x

        if n < 0:
            x = 1 / x
            n = -n

        return recur(n)
