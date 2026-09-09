class Solution:
    def projectionArea(self, grid):
        top = 0
        front = 0
        side = 0

        for i in range(len(grid)):
            row_max = 0

            for j in range(len(grid[0])):
                # Top view
                if grid[i][j] > 0:
                    top += 1

                # Maximum height in the row
                row_max = max(row_max, grid[i][j])

            front += row_max

        # Maximum height in each column
        for j in range(len(grid[0])):
            col_max = 0

            for i in range(len(grid)):
                col_max = max(col_max, grid[i][j])

            side += col_max

        return top + front + side

  
