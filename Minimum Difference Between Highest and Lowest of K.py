class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_diff = float("inf")

        for left in range(len(nums) - k + 1):
            right = left + k - 1
            difference = nums[right] - nums[left]
            min_diff = min(min_diff, difference)

        return min_diff
