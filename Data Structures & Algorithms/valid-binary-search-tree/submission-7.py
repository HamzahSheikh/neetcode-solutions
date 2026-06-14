# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, max_past:int, min_past:int):
            
            if root:

                if root.val >= max_past or root.val <= min_past:
                    return False

                leftValid = dfs(root.left, root.val, min_past)
                rightValid = dfs(root.right, max_past, root.val)

                return leftValid and rightValid
            
            return True

        return dfs(root, float('inf'), float('-inf'))
                
                