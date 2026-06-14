class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        ans = 0
        stack = []

        for x in tokens:

            if x == '+':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a+b)
            elif x == '-':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b-a)
            elif x == '*':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a*b)
            elif x == '/':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b/a) 
            else:
                stack.append(int(x))

            print(stack)

        return int(stack[0])