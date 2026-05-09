def reverse_string_manual(s):
    char =list(s)

    left, right = 0 , len(char) -1
    while left < right:
        char[left], char[right] = char[right], char[left]
        left  += 1
        right -= 1
    return "".join(char)

print(reverse_string("hello"))         # "olleh"
print(reverse_string_manual("hello"))
