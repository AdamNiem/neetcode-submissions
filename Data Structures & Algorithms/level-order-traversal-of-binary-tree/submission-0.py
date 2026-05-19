# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #so we want to return a list where each item is a list of values left to right for that level
        # is this a dfs/bfs recursive soln or an iterative one?
        # I think it might be an iterative one since bfs and dfs work on subtree level?
        # actually probably bfs/dfs and use some level param to keep track of level?
        #yup its bfs

        output = []
        
        def bfs(root, level=0):

            if root is None:
                return
            
            if len(output) < level + 1: 
                output.append([])

            output[level].append(root.val)

            bfs(root.left, level+1)
            bfs(root.right, level+1)

        bfs(root, 0)
        
        return output