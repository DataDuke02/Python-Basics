arr = list(map(int,input("Enter Numbers : ").split()))

is_sorted = True

for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        is_sorted = False
        break

if is_sorted:
    print("Array is Sorted")
else:
    print("Array is Not Sorted")

if is_sorted == False:
    arr = arr.sort()
    print("Sorted Array : ",arr)
