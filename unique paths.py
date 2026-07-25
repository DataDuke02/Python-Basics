class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a single row of size n with 1s
        # There is only 1 way to reach any cell in the first row
        row = [1] * n
        
        # Iterate through the remaining m - 1 rows
        for i in range(1, m):
            for j in range(1, n):
                # The current cell value is its previous value (above) 
                # plus the value of the cell to its left
                row[j] += row[j - 1]
                
        return row[-1]
