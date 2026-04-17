arr = [4,5,6,1,8,3,4,83,4,3,41,8,3,1,83]

for i in arr:
    print(i,end=' ')

arr = [4,5,6,1,8,3,4,83,4,3,41,8,3,1,83]

for i in range(len(arr)-1, -1, -1):
    print(arr[i],end=" ")

for value in arr:
    print(value)

target = 41
found = False

for i in arr:
    if arr[i]== target:
        target += arr[i]
        found = True
        break


for i in range(len(arr)):
    arr[i]+=5

for num in arr:
    print(num,end=" ")

    
