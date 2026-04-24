#Find the maximum sum of a contiguous subarray.

def maxSubArray(nums):
    max_sum = curr = nums[0]
    for num in nums[1:]:
        curr = max(num, curr + num)
        max_sum = max(max_sum, curr)
    return max_sum

nums = [11,1,3,5,8,9,6]

print(maxSubArray(nums))
