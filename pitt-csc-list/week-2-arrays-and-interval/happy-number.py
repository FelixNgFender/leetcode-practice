def isHappy(n):
    seen = set()
    seen.add(n)
    while n != 1:
        sum = 0
        temp = n
        while temp:
            digit = temp % 10
            sum += digit * digit
            temp //= 10
        n = sum
        if n in seen:
            return False
        seen.add(n)
    return True


print(isHappy(19))

print(isHappy(2))
