def threeSum(nums):
    resSet = set()
    for i in range(len(nums)):
        target = 0 - nums[i]
        diff = {}
        for j in range(i + 1, len(nums)):
            if nums[j] in diff:
                triplet = [nums[i], nums[j], nums[diff[nums[j]]]]
                triplet.sort()
                resSet.add(tuple(triplet))
            else:
                diff[target - nums[j]] = j
    res = []
    for triplet in resSet:
        accum = []
        for e in triplet:
            accum.append(e)
        res.append(accum)
    return res


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))

nums = [0, 1, 1]
print(threeSum(nums))

nums = [0, 0, 0]
print(threeSum(nums))
