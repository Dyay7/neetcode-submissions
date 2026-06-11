# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if not root or not p or not q:
            return None

        if max(p.val, q.val) < root.val: # check if the max of the values is less than the root val -> we go left
            return self.lowestCommonAncestor(root.left, p , q)
        elif min(p.val, q.val) > root.val:# check if the max of the values is higher than the root val -> we go right
            return self.lowestCommonAncestor(root.right, p, q)
        else: # in the LCA, the max of p and q is higher than root.val and the min is lower than root.val
            return root