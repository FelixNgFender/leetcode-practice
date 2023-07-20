def twoSum(nums, target):
    diff = {}
    for i, n in enumerate(nums):
        if n in diff:
            return [diff[n], i]
        diff[target - n] = i


nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))

nums = [3, 2, 4]
target = 6
print(twoSum(nums, target))

nums = [3, 3]
target = 6
print(twoSum(nums, target))
