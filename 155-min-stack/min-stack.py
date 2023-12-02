class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        if self.st:
            self.st.insert(0,[val, min(val, self.st[0][1])])
        else:
            self.st.insert(0,[val, val])
    def pop(self) -> None:
        if self.st:
            self.st.pop(0)

    def top(self) -> int:
        if self.st:
            return self.st[0][0]
        return

    def getMin(self) -> int:
        if self.st:
            return self.st[0][1]
        return


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()