# Generate all permutations of a given list of numbers.

def permute(nums):
    result = []
    backtrack(nums, [], result)
    return result

def backtrack(nums, current, result):
    if len(current) == len(nums):
        result.append(list(current))
        return
    for num in nums:
        if num in current: continue
        current.append(num)
        backtrack(nums, current, result)
        current.pop()
