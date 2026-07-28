class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return (
            n > 0 and
            (n & (n - 1)) == 0 and
            (n - 1) % 3 == 0
        )

print(Solution().isPowerOfFour(16))  # True
print(Solution().isPowerOfFour(5))   # False
print(Solution().isPowerOfFour(1))   # True
print(Solution().isPowerOfFour(64))  # True
print(Solution().isPowerOfFour(8))   # False
