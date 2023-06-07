def maxSubArray(nums):
    pre = [0]
    acc = 0
    for i in range(len(nums)):
        acc += nums[i]
        pre.append(acc)
    # The rest is buy and sell stock
    l, r = 0, 1
    maxDiff = pre[r] - pre[l]
    while r < len(pre):
        curr = pre[r] - pre[l]
        if curr < 0:
            l = r
        if curr > maxDiff:
            maxDiff = curr
        r += 1
    return maxDiff

def optimizedMaxSubArray(nums):
    # Kadane's algorithm
    curr = 0
    max = float('-inf')
    for n in nums:
        curr += n
        if curr > max:
            max = curr
        if curr < 0:
            curr = 0
    return max

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))

nums = [1]
print(maxSubArray(nums))

nums = [5,4,-1,7,8]
print(maxSubArray(nums))

nums = [-1]
print(maxSubArray(nums))

nums = [-2, -1]
print(maxSubArray(nums))