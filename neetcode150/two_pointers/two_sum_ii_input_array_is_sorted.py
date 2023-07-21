def twoSum(numbers, target):
    l, r = 0, len(numbers) - 1
    while l < r:
        currSum = numbers[l] + numbers[r]
        if currSum > target:
            r -= 1
        elif currSum < target:
            l += 1
        else:
            return [l + 1, r + 1]


numbers = [2, 7, 11, 15]
target = 9
print(twoSum(numbers, target))

numbers = [2, 3, 4]
target = 6
print(twoSum(numbers, target))

numbers = [-1, 0]
target = -1
print(twoSum(numbers, target))
