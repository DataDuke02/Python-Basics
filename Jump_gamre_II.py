#Given an array of non-negative integers nums, where each element represents
#your maximum jump length from that position, return the minimum number of jumps to
#reach the last index

def jump(nums):
    jumps, current_end, farthest = 0, 0, 0
    for i in range(len(nums)- 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
    return jumps
