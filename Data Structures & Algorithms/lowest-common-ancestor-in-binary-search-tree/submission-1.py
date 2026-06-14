# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:


        def dfs(root, target: int, parents: set) -> set:
            
            if not root:
                return []
            
            if root.val == target:
                parents.add(root)
                return parents
            
            parents.add(root)

            if target > root.val:
                return dfs(root.right, target, parents)
            else:
                return dfs(root.left, target, parents)
            
        
        parents_a = dfs(root, p.val, {p})
        parents_b = dfs(root, q.val, {q})

        common = parents_a.intersection(parents_b)

        min_val = float('inf')
        min_node = None

        for x in common:
            print(x.val)
            if x.val <= min_val and (p.val <= x.val <= q.val) or (q.val <= x.val <= p.val):
                min_val = x.val
                min_node = x

        return min_node  