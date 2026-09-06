class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0

n = 2 → Alice chooses 1 → Bob gets 1 → Alice wins
n = 3 → Alice can only choose 1 → Bob gets 2 → Bob wins
n = 4 → Alice chooses 1 → Bob gets 3 → Alice eventually wins
