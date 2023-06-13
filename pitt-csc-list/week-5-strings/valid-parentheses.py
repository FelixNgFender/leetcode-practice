def isValid(s):
    if len(s) <= 1 or len(s) % 2 == 1:
        return False
    stack = []
    open = ["(", "[", "{"]
    close = [")", "]", "}"]
    for c in s:
        if len(stack) == 0 and c in close:
            return False
        if c in open:
            stack.append(c)
        else:
            top = stack.pop()
            type = close.index(c)
            if top != open[type]:
                return False
    return len(stack) == 0


s = "()"
print(isValid(s))

s = "()[]{}"
print(isValid(s))

s = "(]"
print(isValid(s))
