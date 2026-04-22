"""
def two_sum_brute_force(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):  # avoid duplicate pairs
            if numbers[i] + numbers[j] == target:
                return [i, j]
"""

def two_sum_optimal(numbers, target):
    # Create a hash table (dictionary) to store numbers and their indices
    num_dict = {}

    for i in range(len(numbers)):
        # Store each number as a key, along with its index
        num_dict[numbers[i]] = i

        # Check if the difference between the target and this number is already in the hash table
        if target - numbers[i] in num_dict:
            return [num_dict[target - numbers[i]], i]

    # If no pair is found, return None (or raise an exception)
    return None

# Test the function
numbers = [2, 7, 11, 15]
target = 2
print(two_sum_optimal(numbers, target))  # Output: [0, 1]
