class Solution:
    def rob(self, nums: List[int]) -> int:

        def backtrack(integer, houses: List[int], memo) -> int:
            
            if integer >= len(houses):
                return 0
            
            if integer in memo:
                return memo[integer]

            #if we rob the first house, we cant rob the last one
            total1 = houses[integer] + backtrack(integer+2, houses, memo)
            total2 = backtrack(integer+1, houses, memo)

            totalmax = max(total1, total2)

            memo[integer] = totalmax

            return totalmax

        if len(nums) == 1:
            return nums[0]

        return max(backtrack(0, nums[:-1], {}),
           backtrack(0, nums[1:], {}))
        