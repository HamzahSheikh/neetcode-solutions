class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for x in s:
            
            if x == '(' or x == '{' or x == '[':
                stack.append(x)
            else:
                if len(stack) == 0:
                    return False
                
                top = stack.pop()
                
                if x == ')' and top != '(':
                    return False
                if x == '}' and top != '{':
                    return False
                if x == ']' and top != '[':
                    return False

        return len(stack) == 0
                    
        