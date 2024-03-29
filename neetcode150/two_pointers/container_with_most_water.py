def maxArea(height):
    l, r = 0, len(height) - 1
    maxArea = 0
    while l < r:
        maxArea = max(maxArea, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return maxArea


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))

height = [1, 1]
print(maxArea(height))
