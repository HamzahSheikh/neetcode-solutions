class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        ans = []

        def dfs(total, i, path):
            
            if total == target:
                ans.append(path[:])
                return

            for index in range(i, len(candidates)):
                if index > i and candidates[index] == candidates[index - 1]:
                    continue
                if total + candidates[index] > target:
                    return

                path.append(candidates[index])
                dfs(total + candidates[index], index+1, path)
                path.pop()
            
            return

        dfs(0, 0, [])

        return ans
            
        