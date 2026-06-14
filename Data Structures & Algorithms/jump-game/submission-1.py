class Solution:
    def canJump(self, nums: List[int]) -> bool:

        goal = len(nums) - 1

        for x in range(len(nums) - 2, -1, -1):
            val = nums[x]
            if val >= (goal - x):
                goal = x

        if goal == 0:
            return True 
            
        return False       