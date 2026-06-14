# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        ans = 0

        def dfs(root, max_parent: int):
            nonlocal ans

            if root:
                if root.val >= max_parent:
                    ans += 1

                new_max = max(max_parent, root.val)
                dfs(root.left, new_max)
                dfs(root.right, new_max)

        dfs(root, float('-inf'))

        return ans
        