from math import gcd
from collections import Counter

class Solution:
    def hasGroupsSizeX(self, deck):
        count = Counter(deck)

        x = 0

        for value in count.values():
            x = gcd(x, value)

        return x >= 2

  """
  deck = [1, 1, 2, 2, 2, 2]

1 → 2
2 → 4

gcd(2, 4) = 2

[1, 1]
[2, 2]
[2, 2]
  """
