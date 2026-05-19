# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")

        def dfs(root):
            nonlocal max_sum

            if root:
                #so first get to very left most node
                dfs(root.left)
                dfs(root.right)

                #case where we consider split occurs here
                left = self.getMax(root.left)
                right = self.getMax(root.right)
                max_sum = max(root.val + left + right, max_sum)

                #now return case where sp

        dfs(root)

        return max_sum

    def getMax(self, root: Optional[TreeNode]) -> int:
            if root is None:
                return 0

            left = self.getMax(root.left)
            right = self.getMax(root.right)
            path = root.val + max(left, right)

            return max(path, 0)


