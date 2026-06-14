class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        ans = []
        n = 0

        for i, x in enumerate(nums):
            
            if i > 0 and x == nums[i-1]:
                continue
            
            target = 0 - x
            p1 = i+1
            p2 = len(nums) - 1

            while p2 > p1:

                val = nums[p1] + nums[p2]

                if target == val:
                    ans.append([nums[i], nums[p1], nums[p2]])
                    p1+=1

                    while nums[p1] == nums[p1-1] and p2 > p1:
                        p1+=1
                
                if target > val:
                    p1+=1
                else:
                    p2-=1

        return ans
            

            