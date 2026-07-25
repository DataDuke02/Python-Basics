import math

class Solution:
    def (self, m: int, n: int) -> int:
        # Calculate C(m + n - 2, m - 1)
        return math.comb(m + n - 2, m - 1)
