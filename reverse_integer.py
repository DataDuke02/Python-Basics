class Solution:
    def reverse(self, x: int) -> int:
        # Define 32-bit signed integer boundaries
        MIN_INT, MAX_INT = -2**31, 2**31 - 1
        
        # Determine the sign and work with the absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        reversed_num = 0
        while x > 0:
            # Pop the last digit
            digit = x % 10
            # Remove the last digit from x
            x //= 10
            
            # Check for overflow before multiplying
            if reversed_num > (MAX_INT - digit) // 10:
                return 0
                
            reversed_num = reversed_num * 10 + digit
            
        return sign * reversed_num
