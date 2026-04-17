# At beginning
# Insert
arr = [4,6,74,6,7,7,5,4,5,9,1,96,21,74]
element = 50
print(len(arr))
arr.insert(0,element)

for i in range(len(arr)):
    print(arr[i],end=" ")
# Custom Insert

arr1 = [4,6,74,6,7,7,5,4,5,9,1,96,21,74]
n=13
element = 50

for i in range(n-1,-1,-1):
    arr1[i+1] = arr1[i]


arr1[0] = element

for i in range(n+1):
    print(arr1[i],end=" ")
