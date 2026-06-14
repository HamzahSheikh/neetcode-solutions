class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        combos = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        ans = []

        def backtracking(path, remaining):
            
            if len(remaining) == 0:
                if path:
                    ans.append(path)
                return

            curr = remaining[0]
            left = remaining[1:]

            combo = combos[curr]
            
            for i in range(0, len(combo)):
                num = combo[i]
                path += num

                backtracking(path, left)

                #GO BACK
                path = path[:-1]

        backtracking("", digits)
        return ans
                
                
                
        