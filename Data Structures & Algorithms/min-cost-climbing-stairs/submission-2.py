class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
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

