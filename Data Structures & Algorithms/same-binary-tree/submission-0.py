# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Case 1: both nodes are None → trees match here
        if not p and not q:
            return True

        # Case 2: one is None OR values differ → trees differ, stop immediately
        if not p or not q or p.val != q.val:
            return False

        # Case 3: values match → recurse
        # Python short-circuits: if left is False, right is never evaluated
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
