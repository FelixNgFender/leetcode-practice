def maxArea(height):
    l, r = 0, len(height) - 1
    currMax = 0
    while l < r:
        currArea = min(height[l], height[r]) * (r - l)
        if currMax < currArea:
            currMax = currArea
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1
    return currMax


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))

height = [1, 1]
print(maxArea(height))
