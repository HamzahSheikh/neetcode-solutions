class Solution:
    def permute(self, nums):
        ans = []

        def backtrack(path, remaining):
            if not remaining:
                ans.append(path[:])
                return

            for i in range(len(remaining)):
                path.append(remaining[i])

                backtrack(path, remaining[:i] + remaining[i+1:])

                path.pop()

        backtrack([], nums)
        return ans
        