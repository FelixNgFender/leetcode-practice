def findMin(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return nums[lo]

nums = [3, 4, 5, 1, 2]
print(findMin(nums))

nums = [2, 3, 4, 5, 1]
print(findMin(nums))

nums = [4,5,6,7,0,1,2]
print(findMin(nums))

nums = [11,13,15,17]
print(findMin(nums))
