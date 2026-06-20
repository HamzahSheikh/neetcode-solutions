class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # what is the greedy best spot to start?
        # maximize fuel fill, minimize fuel consomption
        if sum(gas) < sum(cost):
            return -1
        
        totalNetFuel = 0
        optimal = 0

        for i in range(len(gas)):
            
            c_gas = gas[i]
            c_cost = cost[i]

            totalNetFuel = c_gas - c_cost + totalNetFuel

            if totalNetFuel < 0:
                totalNetFuel = 0
                optimal = i + 1

        return optimal


