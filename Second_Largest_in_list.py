n = [545,56,54,564,654,65,45,454,5,45,4]
#largest = 0
#sec_largest = 0
largest = sec_largest = float('-inf')

for num in n:
    if num > largest:
        sec_largest = largest
        largest = num
    elif num > sec_largest and num != largest:
        sec_largest = num

print(sec_largest)

if sec_largest == float('-inf'):
    print("No second largest element")
else:
    print("Second largest:", sec_largest)


n = list(set(n))   # remove duplicates
n.sort()
