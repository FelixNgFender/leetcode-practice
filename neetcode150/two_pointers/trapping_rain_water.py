def trap(height):
    if len(height) <= 2:
        return 0

    n = len(height)
    maxLeft, maxRight = height[0], height[n - 1]
    left, right = 1, n - 2
    ans = 0

    while left <= right:
        if maxLeft < maxRight:
            if height[left] > maxLeft:
                maxLeft = height[left]
            else:
                ans += maxLeft - height[left]
            left += 1
        else:
            if height[right] > maxRight:
                maxRight = height[right]
            else:
                ans += maxRight - height[right]
            right -= 1

    return ans


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height))

height = [4, 2, 0, 3, 2, 5]
print(trap(height))
