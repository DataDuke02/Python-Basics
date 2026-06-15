def find_anagrams(s, p):
    if len(p) > len(s):
        return []

    result = []
    p_count = {}
    w_count = {}

    for char in p:
        p_count[char] = p_count.get(char, 0) + 1

    # Build first window
    for i in range(len(p)):
        w_count[s[i]] = w_count.get(s[i], 0) + 1

    if w_count == p_count:
        result.append(0)

    # Slide the window
    for i in range(len(p), len(s)):
        # Add new right character
        w_count[s[i]] = w_count.get(s[i], 0) + 1

        # Remove old left character
        left_char = s[i - len(p)]
        w_count[left_char] -= 1
        if w_count[left_char] == 0:
            del w_count[left_char]

        if w_count == p_count:
            result.append(i - len(p) + 1)

    return result

print(find_anagrams("cbaebabacd", "abc"))  # [0, 6]
