class Solution:
    def maxCount(self, m: int, n: int, ops):
        if not ops:
            return m * n

        min_row = m
        min_col = n

        for op in ops:
            min_row = min(min_row, op[0])
            min_col = min(min_col, op[1])

        return min_row * min_col


Input:
m = 3
n = 3
ops = [[2,2],[3,3]]

Output:
4
