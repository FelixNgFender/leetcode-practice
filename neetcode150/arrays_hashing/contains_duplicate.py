def containsDuplicate(nums):
    vis = set()
    for n in nums:
        if n in vis:
            return True
        vis.add(n)
    return False


print(containsDuplicate([1, 2, 3, 1]))

print(containsDuplicate([1, 2, 3, 4]))

print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
