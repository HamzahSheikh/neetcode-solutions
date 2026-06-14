class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for x in tokens:
            if x == '+':
                a = stack.pop()
                b = stack.pop()
                ans = b + a 
                stack.append(ans)
            elif x == '-':
                a = stack.pop()
                b = stack.pop()
                ans = b - a 
                stack.append(ans)
            elif x == '*':
                a = stack.pop()
                b = stack.pop()
                ans = b * a 
                stack.append(ans)
            elif x == '/':
                a = stack.pop()
                b = stack.pop()
                ans = b / a 
                stack.append(int(ans))
            else:
                stack.append(int(x))

        return stack.pop() 