class Solution:
    def jump(self, nums: List[int]) -> int:

        #[2,4,1,1,1,1]
        
        r = 0
        jumps = 0
        maxSeen = nums[0] #2


        while r < len(nums)-1: # < 5

            potential = maxSeen
            
            for i in range(0, potential): # 0 to 2
                r+=1

                if r >= len(nums):
                    break

                maxSeen = max(nums[r], maxSeen-1) 
            
            # r -> 2
            jumps+=1
        
        return jumps

        

        