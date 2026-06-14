class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minPrice = prices[0]
        maxProfit = 0


        for x in prices:
            minPrice = min(minPrice, x)
            maxProfit = max(maxProfit, x - minPrice)

        return maxProfit