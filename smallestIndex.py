class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        for i, num in enumerate(nums):
            # Calculate the sum of digits for the current number
            digit_sum = 0
            temp = num
            while temp > 0:
                digit_sum += temp % 10
                temp //= 10
            
            # If the calculated digit sum equals the current index, return it
            if digit_sum == i:
                return i
                
        # Return -1 if no such index satisfies the condition
        return -1
