class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []

        def backtracking(path, opened, needclosing):

            if len(path) == n*2: # 0 == 2 --> FALSE
                ans.append(path)
                return

            if opened < n: # 0 < 0 --> FALSE
                path += "("
                backtracking(path, opened+1, needclosing+1)
                path = path[:-1]

            
            if needclosing > 0:
                path += ")"
                backtracking(path, opened, needclosing-1)
                path = path[:-1]

            return


        backtracking("", 0, 0)

        return ans



        