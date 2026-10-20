def maxVowels(s: str, k: int) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Count vowels in the first window of size k
    current_vowels = sum(1 for i in range(k) if s[i] in vowels)
    max_vowels = current_vowels
    
    # Slide the fixed window across the rest of the string
    for i in range(k, len(s)):
        # Add the incoming character
        if s[i] in vowels:
            current_vowels += 1
        # Subtract the outgoing character
        if s[i - k] in vowels:
            current_vowels -= 1
            
        # Update the maximum count found
        if current_vowels > max_vowels:
            max_vowels = current_vowels
            
        # Optimization: cannot exceed k vowels
        if max_vowels == k:
            return k
            
    return max_vowels
