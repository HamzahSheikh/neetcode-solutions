# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        queue = [root]


        while queue:
            curr = queue.pop()
            
            if not curr:
                continue
            
            l = curr.left
            r = curr.right

            curr.left = r
            curr.right = l

            queue.append(l)
            queue.append(r)

        return root

        