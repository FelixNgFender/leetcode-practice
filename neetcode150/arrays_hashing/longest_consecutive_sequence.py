def longestConsecutive(nums):
    numSet = set(nums)
    maxLength = 0
    for n in nums:
        # start of a sequence
        if n - 1 not in numSet:
            length = 0
            while n + length in numSet:
                length += 1
            maxLength = max(maxLength, length)
    return maxLength


nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums))

nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(longestConsecutive(nums))
