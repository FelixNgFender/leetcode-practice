def dailyTemperatures(temperatures):
    # See Techniques sheet on monotonic stack
    # This problem is find next greater element
    # -> use monotonically decreasing stack
    stack = []  # index
    res = [0] * len(temperatures)
    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            res[stack[-1]] = i - stack[-1]
            stack.pop()
        stack.append(i)
    return res


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(temperatures))

temperatures = [30, 40, 50, 60]
print(dailyTemperatures(temperatures))

temperatures = [30, 60, 90]
print(dailyTemperatures(temperatures))
