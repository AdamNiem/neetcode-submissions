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
            queue = [ root ]

            while queue:
                level_vals = []
                #pop items off queue, add to result
                queue_len = len(queue)
                for idx in range(0, queue_len):
                    node = queue[0]
                    level_vals.append(node.val)
                    #then add the children of each item of the queue instead
                    if node.left:
                        queue.append(node.left)
                    
                    if node.right:
                        queue.append(node.right)
                   
                    queue.pop(0)
                res.append(level_vals)

            return res

        return bfs(root)