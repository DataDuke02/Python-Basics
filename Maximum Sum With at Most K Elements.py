class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        values = []

        for i in range(len(grid)):
            row = sorted(grid[i], reverse=True)
            values.extend(row[:limits[i]])

        values.sort(reverse=True)

        return sum(values[:k])
