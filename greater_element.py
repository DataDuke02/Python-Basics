def next_greater_element(arr):
    n = len(arr)
    result = [-1] * n      # default all to -1
    stack = []             # stores indices

    for i in range(n):
        # while stack has elements AND current > element at stack top
        while stack and arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            result[idx] = arr[i]   # current is next greater for idx
        stack.append(i)

    return result

print(next_greater_element([4, 5, 2, 10, 8]))    # [5, 10, 10, -1, -1]
