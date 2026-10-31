class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        longest = ""

        for left in range(len(s)):
            seen = set()

            for right in range(left, len(s)):
                seen.add(s[right])

                # Every character must have its opposite case in the set
                nice = all(
                    char.swapcase() in seen
                    for char in seen
                )

                # Use >, not >=, to keep the earliest result in a tie
                if nice and right - left + 1 > len(longest):
                    longest = s[left:right + 1]

        return longest
