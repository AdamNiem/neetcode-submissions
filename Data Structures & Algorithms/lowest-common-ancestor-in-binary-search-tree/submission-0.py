# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # ok so we know this is a dfs problem
        # we want to start from root and work down
        # we record most recent ancestor until we hit both p and q?
        # 

        # might need to do dfs to find both p and q, and then once
        cur = root
        while cur is not None:
            if cur.val == p.val or cur.val == q.val:
                return cur
            if (cur.val > p.val and cur.val < q.val) or (cur.val < p.val and cur.val > q.val):
                return cur
            
            if cur.val < p.val and cur.val < q.val:
                cur = cur.right
            elif cur.val > p.val and cur.val > q.val:
                cur = cur.left
            
