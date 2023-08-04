def isValid(s):
    stack = []
    brackets = {
        "(": ")",
        "[": "]",
        "{": "}",
    }
    for c in s:
        if c in brackets:
            stack.append(c)
        elif not stack or brackets.get(stack[-1]) != c:
            return False
        else:
            stack.pop()
    return len(stack) == 0


s = "()"
print(isValid(s))

s = "()[]{}"
print(isValid(s))

s = "(]"
print(isValid(s))
