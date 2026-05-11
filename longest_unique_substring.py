def longest_unique_substring(s):
    seen = {}       # char → last seen index
    left = 0
    max_len = 0

    for right in range(len(s)):
        char = s[right]

        # If char was seen AND it's inside our current window
        if char in seen and seen[char] >= left:
            left = seen[char] + 1   # shrink window from left

        seen[char] = right          # update last seen index
        max_len = max(max_len, right - left + 1)

    return max_len

print(longest_unique_substring("abcabcbb"))  # 3
print(longest_unique_substring("bbbbb"))     # 1
print(longest_unique_substring("pwwkew"))    # 3
print(longest_unique_substring(""))          # 0
