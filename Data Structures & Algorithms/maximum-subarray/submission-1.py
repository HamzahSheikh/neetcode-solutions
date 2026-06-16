class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currSum = nums[0]
        total = 0

        for x in nums:
            if total < 0:
                total = 0
            
            total += x
            currSum = max(currSum, total)

        return currSum
                


        