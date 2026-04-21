# Remove duplicates

result = []  # Initialize an empty list
seen = set()  # Initialize an empty set for O(1) lookups

for i in arr:  # Iterate over the array
    if not seen.add(i):  # Add i to the set; if it's already present, don't append to result
        result.append(i)

print(result)
