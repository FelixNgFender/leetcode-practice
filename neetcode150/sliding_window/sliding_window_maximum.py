from collections import deque


def maxSlidingWindow(nums, k):
    # monotonically decreasing queue
    res = []
    localMax = deque()  # index
    left = right = 0
    # O(n) O(n)
    while right < len(nums):
        # pop smaller values from q
        while localMax and nums[localMax[-1]] < nums[right]:
            localMax.pop()
        localMax.append(right)

        # remove left val from window
        if left > localMax[0]:
            localMax.popleft()

        if (right + 1) >= k:
            res.append(nums[localMax[0]])
            left += 1
        right += 1

    return res


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(maxSlidingWindow(nums, k))


nums = [1]
k = 1
print(maxSlidingWindow(nums, k))
