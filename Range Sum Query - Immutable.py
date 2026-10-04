class NumArray:

    def __init__(self, nums):
        self.prefix = [0]

        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

"""
nums = [-2, 0, 3, -5, 2, -1]

[0, -2, -2, 1, -4, -2, -3]

sumRange(0, 2)
= prefix[3] - prefix[0]
= 1 - 0
= 1

"""
