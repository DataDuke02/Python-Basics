def subsets(nums):
    result = []
    backtrack(nums, 0, [], result)
    return result

def backtrack(nums, start, current, result):
    result.append(list(current))
    for i in range(start, len(nums)):
        current.append(nums[i])
        backtrack(nums, i + 1, current, result)
        current.pop()
