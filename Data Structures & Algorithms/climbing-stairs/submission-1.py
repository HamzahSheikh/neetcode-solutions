class Solution:
    def climbStairs(self, n: int) -> int:

        dp = {}


        def backtrack(taken) -> int:
            
            if taken in dp:
                return dp[taken]
            
            if taken == n:
                return 1
            
            if taken > n:
                return 0
            
            total = backtrack(taken+1) + backtrack(taken+2)
            dp[taken] = total
            return total
        
        return backtrack(0)
        