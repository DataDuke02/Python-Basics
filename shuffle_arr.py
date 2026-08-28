import random

class Solution:

    def __init__(self, nums):
        self.original = nums[:]
        self.nums = nums[:]

    def reset(self):
        return self.original[:]

    def shuffle(self):
        random.shuffle(self.nums)
        return self.nums[:]

  Input:
nums = [1, 2, 3]

shuffle() → [3, 1, 2]
shuffle() → [2, 3, 1]

reset() → [1, 2, 3]
