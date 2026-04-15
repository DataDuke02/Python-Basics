def Binary_Search(arr,target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid]< target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = [5,8,6,2,10,24,55,83,64,20]
x = 83

print("Found at Index : ",Binary_Search(arr,x))
