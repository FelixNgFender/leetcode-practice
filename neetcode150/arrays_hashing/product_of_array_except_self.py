def productExceptSelf(nums):
    res = [1] * len(nums)
    pre = 1
    for i in range(0, len(nums)):
        res[i] = pre
        pre *= nums[i]
    suf = 1
    for j in range(len(nums) - 1, -1, -1):
        res[j] *= suf
        suf *= nums[j]
    return res


nums = [1, 2, 3, 4]
print(productExceptSelf(nums))

nums = [-1, 1, 0, -3, 3]
print(productExceptSelf(nums))
