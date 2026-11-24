from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
            
        char_counts = Counter(magazine)
        
        for char in ransomNote:
            if char_counts[char] <= 0:
                return False
            char_counts[char] -= 1
            
        return True
