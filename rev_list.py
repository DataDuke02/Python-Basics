#  Reverse a list in-place (no extra space)
def reverse_in_place(arr):
    left = 0
    right = len(arr) - 1

    # Iterate through the list, swapping elements from both ends
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
print(reverse_in_place(arr))  # Output: [5, 4, 3, 2, 1]
