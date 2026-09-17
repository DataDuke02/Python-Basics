class Solution:
    def oddCells(self, m: int, n: int, indices):
        rows = [0] * m
        cols = [0] * n

        for r, c in indices:
            rows[r] += 1
            cols[c] += 1

        count = 0

        for i in range(m):
            for j in range(n):
                if (rows[i] + cols[j]) % 2 == 1:
                    count += 1

        return count

  """
Rows:
row 0 → 1
row 1 → 1

Columns:
col 0 → 0
col 1 → 2
  """
