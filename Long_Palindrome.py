#Find the longest palindromic substring in a given string

def longestPalindrome(s):
    def expandAroundCenter(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    start, maxLength = 0, 1
    for i in range(len(s)):
        len1 = expandAroundCenter(s, i, i)
        len2 = expandAroundCenter(s, i, i + 1)
        length = max(len1, len2)
        if length > maxLength:
            maxLength = length
            start = i- (maxLength- 1) // 2
    return s[start:start + maxLength]
