class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []

        def backtrack(curr, index):
            
            if index == len(nums):
                ans.append(curr[:])
                return

            curr.append(nums[index])
            backtrack(curr, index+1)
            curr.pop()

            backtrack(curr, index+1)
                

        backtrack([], 0)

        return ans
