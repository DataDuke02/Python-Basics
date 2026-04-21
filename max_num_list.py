# Define the array of numbers
arr = [7,5,4,0,8,2,7,5,18,562,7,82,7,8,54,8,56,2,74,89,2,4,45,2,5,8,41,2,8,74,59,62,1,7,8,565]

# Initialize max with a smaller value (e.g., the smallest possible integer in Python)
max_val = float('-inf')  # Negative infinity

# Iterate over each element in the array
for i in arr:
    # Check if current element is greater than max_val
    if i > max_val:  # Corrected condition to update max_val
        max_val = i  # Update max_val with the new maximum value

print(max_val)  # Print the final maximum value
