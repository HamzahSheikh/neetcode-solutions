class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

#               _
#         1          2
#     2       3   3     4
# 3       4  
        dp = {}

        def backtrack(index) -> int:

            if index >= len(cost):
                return 0
            
            if index in dp:
                return dp[index]

            cheapestPath = cost[index] + min(backtrack(index+1), backtrack(index+2))
            
            dp[index] = cheapestPath

            return cheapestPath


        return min(backtrack(0), backtrack(1))

