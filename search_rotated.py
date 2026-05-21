def search_rotated(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        # Left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1    # target in left half
            else:
                left = mid + 1     # target in right half
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1     # target in right half
            else:
                right = mid - 1    # target in left half

    return -1

print(search_rotated([4,5,6,7,0,1,2], 0))   # 4
print(search_rotated([4,5,6,7,0,1,2], 3))   # -1
print(search_rotated([1], 0))                # -1
