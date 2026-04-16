def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1): # 4 - 1 = 3 arr[3] = 9 ,
        for j in range(n-i-1): # 4 - 3 - 1 = 0 arr[0] = arr[-1] == 5
            if arr[i] > arr[j+1]: # 9 > 5
                arr[j], arr[j+1] = arr[j+1],arr[j]  # 9, 5 = 5, 9 #5, 9
    return arr #5,9

arr = [5,2,9,1]
print("Sorted :",bubble_sort(arr))
print(len(arr))
print(arr[0])
