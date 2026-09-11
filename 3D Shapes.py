class Solution:
    def surfaceArea(self, grid):
        area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                height = grid[i][j]

                if height == 0:
                    continue

                # Top + bottom
                area += 2

                # Front
                if i == 0:
                    area += height
                else:
                    area += max(0, height - grid[i - 1][j])

                # Back
                if i == len(grid) - 1:
                    area += height
                else:
                    area += max(0, height - grid[i + 1][j])

                # Left
                if j == 0:
                    area += height
                else:
                    area += max(0, height - grid[i][j - 1])

                # Right
                if j == len(grid[0]) - 1:
                    area += height
                else:
                    area += max(0, height - grid[i][j + 1])

        return area


"""
Top + Bottom = 2

Current stack = 4
Neighbor stack = 2

Visible area = 4 - 2 = 2

Current = 2
Neighbor = 4

Visible area = 0

max(0, current_height - neighbor_height)
"""
