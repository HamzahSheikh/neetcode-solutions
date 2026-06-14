class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        ans = []    # [] | [1] | [1, 1]
        nums.sort() #[1, 1, 2]


        def backtrack(path, index): # [], 0 | [1] , 1 | [1, 1], 2 | [1, 1, 2], 3

            if index > len(nums): # FALSE | FALSE | FALSE | TRUE
                return

            seen = set() # {} | {} | {}

            ans.append(path[:]) 

            for i in range(index, len(nums)): # 0 to 3 | 1 to 3 | 2 to 3
                curr = nums[i] # 1 | 1 | 2
                
                if i > index and curr in seen: # FALSE | FALSE | FALSE
                    continue

                seen.add(curr) 
                
                path.append(curr) #[1] | [1, 1] | [1, 1, 3]
                backtrack(path[:], i+1) #[1],  1 | [1, 1], 2 | [1, 1 , 2], 3
                path.pop() #[], [1], [1, 1]

        backtrack([], 0)

        return ans

        