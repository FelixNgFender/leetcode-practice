def threeSum(nums):
    res = []
    nums.sort()

    for i, n in enumerate(nums):
        # avoid duplicates
        if i > 0 and n == nums[i - 1]:
            continue

        # two sum on sorted subarray
        l, r = i + 1, len(nums) - 1
        target = 0 - n
        while l < r:
            currSum = nums[l] + nums[r]
            if currSum < target:
                l += 1
            elif currSum > target:
                r -= 1
            else:
                res.append([n, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1

    return res


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))

nums = [0, 1, 1]
print(threeSum(nums))

nums = [0, 0, 0]
print(threeSum(nums))

nums = [0, 0, 0, 0]
print(threeSum(nums))

nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
