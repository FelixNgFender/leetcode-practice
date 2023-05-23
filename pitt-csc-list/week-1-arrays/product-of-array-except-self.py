def productExceptSelf(nums):
    prefix = [0] * len(nums)
    postfix = [0] * len(nums)
    acc = 1
    for i, x  in enumerate(nums):
        acc *= x
        prefix[i] = acc
    acc = 1
    for i in range(len(nums) -1, -1, -1):
        acc *= nums[i]
        postfix[i] = acc
    ans = []
    for i in range(len(nums)):
        if i == 0:
            ans.append(postfix[1])
        elif i == len(nums) - 1:
            ans.append(prefix[-2])
        else:
            ans.append(prefix[i - 1] * postfix[i + 1])
    return ans

def optimizedProductExceptSelf(nums):
    # Save prefix and postfix directly in res
    res=[1] * len(nums)
    pre = 1
    for i in range(len(nums)):
        res[i] = pre
        pre *= nums[i]
    post = 1
    for j in range (len(nums) - 1, -1 , -1):
        res[j] *= post
        post *= nums[j]
    return res        

nums = [1, 2, 3, 4]
print(productExceptSelf(nums))

nums = [-1,1,0,-3,3]
print(productExceptSelf(nums))