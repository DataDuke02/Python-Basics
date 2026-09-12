class Solution:
    def addToArrayForm(self, num, k):
        i = len(num) - 1
        carry = k
        result = []

        while i >= 0 or carry > 0:
            if i >= 0:
                carry += num[i]

            result.append(carry % 10)
            carry //= 10
            i -= 1

        return result[::-1]


"""
num = [1, 2, 0, 0]
k = 34

1200 + 34 = 1234

[1, 2, 3, 4]
"""
