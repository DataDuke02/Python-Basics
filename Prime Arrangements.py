class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7

        def isPrime(num):
            if num < 2:
                return False

            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False

            return True

        prime_count = 0

        for i in range(1, n + 1):
            if isPrime(i):
                prime_count += 1

        non_prime_count = n - prime_count

        prime_factorial = 1
        for i in range(1, prime_count + 1):
            prime_factorial *= i
            prime_factorial %= MOD

        non_prime_factorial = 1
        for i in range(1, non_prime_count + 1):
            non_prime_factorial *= i
            non_prime_factorial %= MOD

        return (prime_factorial * non_prime_factorial) % MOD
