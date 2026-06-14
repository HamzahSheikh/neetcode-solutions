class Solution:
    def partition(self, s: str) -> List[List[str]]:

        ans = []

        def backtrack(path, remaining):

            if len(remaining) < 1:
                
                if remaining:
                    path.append(remaining)
                ans.append(path[:])
                return
            
            for i in range(1, len(remaining)+1):
                before = remaining[:i] # "bb"
                after = remaining[i:]  # ""

                #check if before is valid
                if valid_palindrome(before):
                    path.append(before)
                    backtrack(path[:], after)
                    path.pop()

        def valid_palindrome(word) -> bool:

            a = 0
            b = len(word)-1

            while a < b:
                if word[a] != word[b]:
                    return False
                a+=1
                b-=1
            
            return True

        backtrack([], s)

        return ans