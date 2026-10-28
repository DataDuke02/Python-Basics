from typing import List
from math import gcd, lcm

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        max_length = 0

        for left in range(n):
            product = 1
            current_gcd = 0
            current_lcm = 1

            for right in range(left, n):
                num = nums[right]

                product *= num
                current_gcd = gcd(current_gcd, num)
                current_lcm = lcm(current_lcm, num)

                if product == current_gcd * current_lcm:
                    max_length = max(
                        max_length,
                        right - left + 1
                    )

        return max_length
