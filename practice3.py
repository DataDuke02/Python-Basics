#reverse array

arr = [5,6,5,1,5,2,4,9,1,4,3,49,2,4,9,2,1,5,3,5,2,65,4,2]

print(arr[::-1])

rev = []

for i in range(len(arr)-1,-1,-1):
    rev.append(arr[i])

print(rev,end=" ")
#largest value
largest = 0
for i in arr:
    if i > largest:
        largest = i
    else:
        pass

print(largest,end=" ")

# Vowels count
s = "hi thiru how are you are you good how is going man for you"
s.replace(" ","")
vowels = 0
consonants = 0

for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants +=1

print(len(s))
print(vowels)

#Palindrome Check string
s1 = "madam"

if s1 == s1[::-1]:
    print("Palindrome")
else:
    print("not")

#Palindrome check in numbers
n = 878

n = str(n)
if n == n[::-1]:
    print(n)
else:
    print("not")

n1 = 878
org = n1
rev = 0

while n1 >0:
    digit = n1%10
    rev = rev * 10 + digit
    n1 //=10

if org == rev:
    print("Palin")
else:
    print("not")

# Duplicate in array


arr1 = [7,65,2,5,63,8,3,26,2,56,5,6,2,5,6,2,12,78,96,5,4,21,3,4,9,98,2]
freq = {}
duplicate = []
result = []


for i in arr1:
    if i not in result:
        result.append(i)
    else:
        duplicate.append(i)

print(duplicate) # duplicate elements
print(result)  # non duplicate elements

for i in arr1:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for key in freq:
    print(key,":",freq[key])

#print(duplicate)

result1 = []
seen = set()

for i in arr1:
    if i not in seen:
        result1.append(i)
        seen.add(i)

print(result1)
#print(seen)
print(sum(arr1))
