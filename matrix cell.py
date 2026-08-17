class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int):
        result = []

        for r in range(rows):
            for c in range(cols):
                distance = abs(r - rCenter) + abs(c - cCenter)
                result.append((distance, r, c))

        result.sort()

        return [[r, c] for distance, r, c in result]

Input:
rows = 2
cols = 2
rCenter = 0
cCenter = 0

Output:
[[0,0],[0,1],[1,0],[1,1]]

distance = |r - rCenter| + |c - cCenter|
