# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque([root])
        ans = []

        while queue:
            currLevel = queue
            queue = deque()
            level = []

            while currLevel:

                curr = currLevel.popleft()

                if curr:
                    queue.append(curr.left)
                    queue.append(curr.right)
                else:
                    continue

                level.append(curr.val)
            
            if level:
                ans.append(level)
        
        return ans

                

    


        