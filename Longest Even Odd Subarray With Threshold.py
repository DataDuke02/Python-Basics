class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        longest = 0
        current = 0

        for i, num in enumerate(nums):
            if num > threshold:
                current = 0
            elif current == 0:
                if num % 2 == 0:
                    current = 1
            elif num % 2 != nums[i - 1] % 2:
                current += 1
            else:
                current = 1 if num % 2 == 0 else 0

            longest = max(longest, current)

        return longest
