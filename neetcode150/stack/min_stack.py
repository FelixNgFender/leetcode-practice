class MinStack(object):
    def __init__(self):
        self.stack = []
        self.currMin = float("inf")
        self.minHistory = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if val <= self.currMin:
            self.currMin = val
            self.minHistory.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if not self.stack:
            return
        poppedVal = self.stack.pop()
        if poppedVal == self.currMin:
            self.minHistory.pop()
            self.currMin = self.minHistory[-1] if self.minHistory else float("inf")

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.stack:
            return
        return self.currMin


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
