def count_vowels(s):
    if not s:
        return None

    s =s.lower().replace(" ","")
    vowels = 0
    consonant = 0

    for char in s:
        if char.isalpha():
            if char in "aeiou":
                vowels += 1
        else:
            consonant += 1
    return vowels

print(count_vowels("lovetodaysuccessfully"))
