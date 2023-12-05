class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        tem = 0
        for e in tokens:
            if e == '+':
                stack.append(stack.pop() + stack.pop())
            elif e == '-':
                tem = stack.pop()
                stack.append(stack.pop() - tem)
            elif e == '/':
                tem = stack.pop()
                stack.append(int(stack.pop() / tem))
            elif e == '*':
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(e))
        return stack.pop()