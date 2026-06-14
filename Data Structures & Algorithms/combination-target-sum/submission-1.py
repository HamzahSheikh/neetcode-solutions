class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans = []

        def backtrack(path, total, remaining: List[int]):

            if total == target:
                ans.append(path[:])
                return

            if total > target:
                return
            
            while remaining:
                path.append(remaining[0])
                total+=remaining[0]
                backtrack(path, total, remaining[:])
                
                #backtrack!
                path.pop()
                total-=remaining[0]

                #onto the next!
                remaining.pop(0)
                

        backtrack([], 0, nums[:])

        return ans
            
