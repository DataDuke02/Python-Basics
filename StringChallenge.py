def StringChallenge(str):
    # __define-ocg__ Find the maximum number of unique characters
    # between matching characters in the string.

    varFiltersCg = 0
    varOcg = {}

    # Store the indices of each character
    for i, ch in enumerate(str):
        if ch not in varOcg:
            varOcg[ch] = []
        varOcg[ch].append(i)

    # Check every pair of matching characters
    for ch in varOcg:
        positions = varOcg[ch]

        if len(positions) >= 2:
            first = positions[0]
            last = positions[-1]

            unique_chars = set(str[first + 1:last])
            varFiltersCg = max(varFiltersCg, len(unique_chars))

    return varFiltersCg


# Example
print(StringChallenge("ahyjakh"))      # Output: 4
print(StringChallenge("ghececgkaem"))  # Output: 5
