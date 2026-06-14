# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue = deque()
        ans = []

        queue.append(root)


        while queue:
            level = queue
            queue = deque()

            nodesInLevel = []

            while level:
                curr = level.popleft()

                if curr:
                    queue.append(curr.right)
                    queue.append(curr.left)
                    nodesInLevel.append(curr.val)
            
            if nodesInLevel:
                ans.append(nodesInLevel[0])

        return ans
        