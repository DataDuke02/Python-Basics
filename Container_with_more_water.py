# Given an array of heights, find two lines that together with the x-axis form a
# container that holds the most water.

def maxArea(height):
    left, right = 0, len(height)- 1
    max_area = 0
    while left < right:
        width = right- left
        min_height = min(height[left], height[right])
        max_area = max(max_area, width * min_height)
        if height[left] < height[right]:
            left += 1
        else:
            right-= 1
    return max_area
