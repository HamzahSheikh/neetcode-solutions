# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        max_depth = 0

        queue = [[root, 1]]

        while queue:

            curr = queue.pop()
            
            if not curr[0]:
                continue

            depth = curr[1] 
            
            if depth > max_depth:
                max_depth = depth
        
            queue.append([curr[0].left, depth+1])
            queue.append([curr[0].right, depth+1])

        return max_depth

        