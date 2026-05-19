# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(tree, subRoot):
            if not tree and not subRoot:
                return True
            
            if not tree or not subRoot:
                return False

            if tree.val != subRoot.val:
                return False
            
            return (
                sameTree(tree.left, subRoot.left) and
                sameTree(tree.right, subRoot.right)
            )

        if root is None:
            return False
        
        if sameTree(root, subRoot):
            return True

        return ( 
            self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 
        )