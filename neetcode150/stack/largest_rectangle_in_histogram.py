def largestRectangleArea(heights):
    # Build out next and previous smaller element for each index
    # using a mono increasing stack
    next = [len(heights)] * len(heights)
    prev = [-1] * len(heights)
    stack = []  # index, mono increasing
    for i, height in enumerate(heights):
        while stack and height <= heights[stack[-1]]:
            next[stack[-1]] = i
            stack.pop()
        if stack and height > heights[stack[-1]]:
            prev[i] = stack[-1]
        stack.append(i)
    maxHeights = [(next[i] - prev[i] - 1) * heights[i] for i in range(len(heights))]
    return max(maxHeights)


heights = [2, 1, 5, 6, 2, 3]
print(largestRectangleArea(heights))

heights = [2, 4]
print(largestRectangleArea(heights))
