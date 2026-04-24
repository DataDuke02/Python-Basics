def linear_search(arr, target):
    for i in range(len(arr)): # 5
        if arr[i] == target: # 5 == 3, 4 == 3, 3 == 3
            return i
    return -1 # 5 - 1 , 4 - 1

arr = [1,2,3,4,5]
x = 3

print("Found at Index : ",linear_search(arr,x))
