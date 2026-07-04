class Solution:
    def floorSqrt(self, n):
        if n == 0 or n == 1:
            return n

        left = 1
        right = n
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == n:
                return mid

            elif mid * mid < n:
                ans = mid
                left = mid + 1

            else:
                right = mid - 1

        return ans
