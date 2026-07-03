class Solution:
    def isPalindrome(self, n):
        original = abs(n)
        num = original
        rev = 0

        while num > 0:
            rev = rev * 10 + (num % 10)
            num //= 10

        return original == rev
