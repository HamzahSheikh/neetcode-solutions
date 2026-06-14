# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # we check the depth of left and right, if one is > 1 difference, we return False

        even = True

        def dfs(root, h: int):
            
            nonlocal even

            if not root:
                return 0
            
            left = dfs(root.left, h)
            right = dfs(root.right, h)
            
            if abs(left-right) > 1:
                even = False
            
            return 1 + max(left, right)

        dfs(root, 0)
        return even
                
                
                

        