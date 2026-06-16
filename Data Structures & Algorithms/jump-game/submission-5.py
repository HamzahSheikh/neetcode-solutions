class Solution:
    def canJump(self, nums: List[int]) -> bool:

        length = len(nums) -1
        flag = length

        for i in range(length, -1, -1):
            
            needed = flag - i

            if needed > 0 and nums[i] >= needed:
                flag = i

        print(flag)
        
        return flag == 0