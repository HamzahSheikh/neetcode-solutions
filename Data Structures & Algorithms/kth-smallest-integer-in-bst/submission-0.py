# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        orderedNodes = []

        def dfs(root):
            nonlocal orderedNodes

            if root:
                dfs(root.left)
                orderedNodes.append(root.val)
                dfs(root.right)

        dfs(root)
    

        return orderedNodes[k-1]