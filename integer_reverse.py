class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        # Reverse the absolute value as a string
        reversed_num = int(str(abs(x))[::-1]) * sign
        
        # Check if the final result falls outside the 32-bit range
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
            
        return reversed_num
