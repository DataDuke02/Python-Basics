def character_replacement(s, k):
    count = {}
    max_freq = 0
    left = 0
    max_len = 0

    for right in range(len(s)):
        char = s[right]
        count[char] = count.get(char, 0) + 1
        max_freq = max(max_freq, count[char])

        # window size - most frequent = chars to replace
        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

print(character_replacement("AABABBA", 1))  # 4
print(character_replacement("ABAB", 2))     # 4
