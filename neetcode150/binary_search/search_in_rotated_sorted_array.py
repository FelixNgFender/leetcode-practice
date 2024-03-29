def search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < nums[lo]:
            if nums[mid] < target and nums[hi] >= target:
                lo = mid + 1
            else:
                hi = mid - 1
        else:
            if nums[mid] > target and nums[lo] <= target:
                hi = mid - 1
            else:
                lo = mid + 1
    return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(search(nums, target))

nums = [4, 5, 6, 7, 0, 1, 2]
target = 3
print(search(nums, target))

nums = [1]
target = 0
print(search(nums, target))
