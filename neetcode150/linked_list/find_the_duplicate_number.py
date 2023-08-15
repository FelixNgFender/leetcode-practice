def findDuplicate(nums):
    # since num in [1, n] -> can use num -> index mapping
    # as "visited" indicator. If a number 2 marks index
    # 2 as visited, when another 2 is encountered, it would
    # see index 2 is already marked so 2 is the repeat number
    for i in range(len(nums)):
        if nums[abs(nums[i]) - 1] < 0:
            nums = [abs(x) for x in nums]
            return nums[i]
        nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]


nums = [1, 3, 4, 2, 2]
print(findDuplicate(nums))

nums = [3, 1, 3, 4, 2]
print(findDuplicate(nums))
