def maxProduct(nums):
    currProd = 1
    maxProd = float('-inf')
    for n in nums:
        currProd *= n
        if currProd > maxProd:
            maxProd = currProd
        if currProd == 0:
            currProd = 1
    currProd = 1
    for i in range(len(nums) -1, -1, -1):
        currProd *= nums[i]
        if currProd > maxProd:
            maxProd = currProd
        if currProd == 0:
            currProd = 1
    return maxProd

nums = [2, 3, -2, 4]
print(maxProduct(nums))

nums = [-2, 0, -1]
print(maxProduct(nums))

nums = [-2]
print(maxProduct(nums))

nums = [-3, -1, -1]
print(maxProduct(nums))

nums = [3, -1, 4]
print(maxProduct(nums))