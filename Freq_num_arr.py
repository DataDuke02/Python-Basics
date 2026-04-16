arr = list(map(int, input("Enter a numbers : ").split()))
arr.sort()
freq = {}

for num in arr:
    if num in freq:
        freq[num] +=1
    else:
        freq[num] = 1

for key in freq:
    print(key, ":",freq[key])

#input = [5,4,54,4,4,64,64,4,46,4,,9,9,6,5,895,6,65,9,6,659,6,6,59]
