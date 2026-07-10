def is_ugly(n: int) -> bool:
    # Ugly numbers must be positive integers
    if n <= 0:
        return False
        
    # Continuously divide by 2, 3, and 5
    for factor in [2, 3, 5]:
        while n % factor == 0:
            n //= factor  # Integer division to strip the factor
            
    # If it reduces to 1, it's an ugly number
    return n == 1

# --- Test Cases ---
print(is_ugly(6))   # Output: True  (6 = 2 × 3)
print(is_ugly(1))   # Output: True  (1 has no prime factors by convention)
print(is_ugly(14))  # Output: False (14 = 2 × 7, and 7 is not allowed)
