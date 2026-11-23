from typing import List


class Solution:

  def arrayPairSum(self, nums: List[int]) -> int:
    # Sort the array in ascending order
    nums.sort()

    # Sum every second element starting from index 0
    return sum(nums[::2])
