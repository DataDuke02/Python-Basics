from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        longest = 0

        for num in count:
            if num + 1 in count:
                length = count[num] + count[num + 1]
                longest = max(longest, length)

        return longest
