def search(nums, target):
    n = len(nums)
    lo, hi = 0, n - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        elif nums[mid] > target:
            hi = mid - 1
        else:
            return mid

    return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(search(nums, target))

nums = [-1, 0, 3, 5, 9, 12]
target = 2
print(search(nums, target))
