class Solution:
    def thirdLargest(self, arr):
        first = second = third = float('-inf')

        for num in arr:
            if num == first or num == second or num == third:
                continue

            if num > first:
                third = second
                second = first
                first = num

            elif num > second:
                third = second
                second = num

            elif num > third:
                third = num

        if third == float('-inf'):
            return -1

        return third
