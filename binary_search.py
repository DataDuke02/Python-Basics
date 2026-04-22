def brute_force_search(nums, target):
    for num in nums:
        if num == target:
            return True  # found it!
    return False  # not found

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_num = 5
print(brute_force_search(numbers, target_num))  # Output: True

def binary_search(nums, target):
    # Initialize two pointers: start (beginning) and end (end)
    start = 0
    end = len(nums) - 1

    while start <= end:
        # Calculate the middle index
        mid = (start + end) // 2

        # If we found it, return True!
        if nums[mid] == target:
            return True

        # Otherwise, adjust our search space based on whether the target is smaller or larger than the middle element
        elif target < nums[mid]:
            # If target is smaller, move end pointer to mid-1 (we don't need to check the rest of this half)
            end = mid - 1
        else:
            # If target is larger, move start pointer to mid+1 (we only need to check the other half)
            start = mid + 1

    # If we exit the loop without finding it, return False
    return False

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_num = 5
print(binary_search(numbers, target_num))  # Output: True
