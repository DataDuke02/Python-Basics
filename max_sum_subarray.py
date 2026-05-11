def max_sum_subarray(arr, k):
    if len(arr) < k:
        return -1

    # Build first window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide the window
    for i in range(k, len(arr)):
        window_sum += arr[i]       # add new right element
        window_sum -= arr[i - k]   # remove old left element
        max_sum = max(max_sum, window_sum)

    return max_sum

print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))  # 9
print(max_sum_subarray([2, 3, 4, 1, 5], 2))      # 7
print(max_sum_subarray([1, 2], 5))                # -1 (k > array)
