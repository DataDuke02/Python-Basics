class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # 3**19 is 1162261467, the largest power of 3 less than 2**31
        return n > 0 and 1162261467 % n == 0
