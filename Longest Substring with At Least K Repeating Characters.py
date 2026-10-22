class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        for char in set(s):
            if s.count(char) < k:
                parts = s.split(char)

                return max(
                    (self.longestSubstring(part, k) for part in parts),
                    default=0
                )

        return len(s)
