# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # so we know its a dfs problem because i just looked
        # so i guess we just start from root and dfs down until found case where it fails?

        #end case when root becomes None just return True

        def dfs(root, max_val = 1001, min_val = -1001):
            if root is None:
                return True

            if root.val >= max_val or root.val <= min_val:
                return False

            return (
                dfs(root.left, root.val, min_val) and 
                dfs(root.right, max_val, root.val)
            )

        return dfs(root)
