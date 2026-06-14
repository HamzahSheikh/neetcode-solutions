class Solution:
    def findMin(self, nums: List[int]) -> int:

        p1 = 0
        p2 = len(nums) - 1

        while p1 < p2:

            val1 = nums[p1]
            val2 = nums[p2]

            if val1 < val2:
                return val1
            
            p1+=1
            p2-=1

            if val1 > nums[p1]:
                return nums[p1]
            
            if val2 < nums[p2]:
                return val2
        
        return nums[0]
        