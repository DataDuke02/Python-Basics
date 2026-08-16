class Solution:
    def smallestRangeI(self, nums, k):
        minimum = min(nums)
        maximum = max(nums)

        difference = maximum - minimum

        if difference <= 2 * k:
            return 0

        return difference - 2 * k
