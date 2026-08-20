class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0

        while dividend >= divisor:
            value = divisor
            power = 1

            while dividend >= (value << 1):
                value <<= 1
                power <<= 1

            dividend -= value
            result += power

        if negative:
            result = -result

        return result

