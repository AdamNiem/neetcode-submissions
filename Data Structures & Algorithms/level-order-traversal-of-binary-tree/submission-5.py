# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # perfect problem for bfs
        # use a python queue?, ill try list first

        def bfs(root):
            if not root:
                return []

            res = []
            queue = deque()
            queue.append(root)

            while queue:
                level_vals = []
                #pop items off queue, add to result
                queue_len = len(queue)
                
                for idx in range(0, queue_len):
                    node = queue.popleft()
                    if node:
                        level_vals.append(node.val)
                        #then add the children of each item of the queue instead
                        queue.append(node.left)
                        queue.append(node.right)
                if level_vals:
                    res.append(level_vals)

            return res

        return bfs(root)