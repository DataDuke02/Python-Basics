s = "hello how are yu doing this days mines are very dry but i keep going so nothing to worry for now even though there is something to worry"

s = s.strip()

vowels = 0
consonants = 0

for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Total characters:", len(s))
print("Consonants:", consonants)
