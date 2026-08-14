class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}

        count = 0

        for num in range(left, right + 1):
            set_bits = bin(num).count("1")

            if set_bits in primes:
                count += 1

        return count


Input:
left = 6
right = 10

Output:
4

6  = 110  → 2 set bits → prime ✓
7  = 111  → 3 set bits → prime ✓
8  = 1000 → 1 set bit  → not prime
9  = 1001 → 2 set bits → prime ✓
10 = 1010 → 2 set bits → prime ✓
