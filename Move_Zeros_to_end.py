def move_zero_to_end(arr):
    non_zero_index = 0
    for num in arr:
        if num != 0:
            arr[non_zero_index] = num
            non_zero_index += 1
    for i in range(non_zero_index,len(arr)):
        arr[i] = 0
    return arr


arr = [2,5,6,7,0,8,0,9,0]
print(move_zero_to_end(arr))
