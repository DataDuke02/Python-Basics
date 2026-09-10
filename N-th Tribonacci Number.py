class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        a = 0
        b = 1
        c = 1

        for i in range(3, n + 1):
            d = a + b + c
            a = b
            b = c
            c = d

        return c
"""
T0 = 0
T1 = 1
T2 = 1
T3 = 0 + 1 + 1 = 2
T4 = 1 + 1 + 2 = 4
"""
