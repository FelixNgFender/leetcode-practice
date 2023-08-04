def evalRPN(tokens):
    stack = []
    operators = {"+", "-", "*", "/"}
    for token in tokens:
        if token not in operators:
            stack.append(token)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(str(int(eval(operand1 + token + operand2))))
    return int(stack[-1])


tokens = ["2", "1", "+", "3", "*"]
print(evalRPN(tokens))

tokens = ["4", "13", "5", "/", "+"]
print(evalRPN(tokens))

tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(evalRPN(tokens))
