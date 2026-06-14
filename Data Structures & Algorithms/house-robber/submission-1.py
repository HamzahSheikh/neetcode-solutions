class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}

        def backtrack(integer) -> int:

            if integer in memo:
                return memo[integer]

            if integer >= len(nums):
                return 0

            # is it more optimal to rob the current house or next?
            # if I rob this house, then I have to skip the next one
            total1 = nums[integer] + backtrack(integer + 2)
            total2 = backtrack(integer + 1)
            totalmax = max(total1, total2)

            memo[integer] = totalmax

            return totalmax

        return backtrack(0)