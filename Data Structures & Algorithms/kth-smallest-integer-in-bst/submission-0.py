# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #we dont know length of tree 
        #we need to start from max of bst which is the rightmost leaf
        #then need to dfs till we get to leftmost branch

        #this is called inorder dfs i think but in opposite direction

        counter = 0
        val = 0

        def dfs(root):
            nonlocal counter, val
            
            if root:
                dfs(root.left)

                counter += 1
                if counter == k:
                    val = root.val

                dfs(root.right)
        
        dfs(root)

        return val
