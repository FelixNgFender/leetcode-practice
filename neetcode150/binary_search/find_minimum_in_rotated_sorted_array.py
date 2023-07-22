def findMin(nums):
    lo, hi = 0, len(nums) - 1
    res = nums[0]
    while lo <= hi:
        # Base case is searching in a sorted range
        if nums[lo] < nums[hi]:
            res = min(res, nums[lo])
            break
        mid = (lo + hi) // 2
        res = min(res, nums[mid])
        if nums[mid] >= nums[lo]:
            lo = mid + 1
        else:
            hi = mid - 1
    return res


nums = [3, 4, 5, 1, 2]
print(findMin(nums))

nums = [4, 5, 6, 7, 0, 1, 2]
print(findMin(nums))

nums = [11, 13, 15, 17]
print(findMin(nums))
