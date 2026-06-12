# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            # When you go left, the node’s value must be less than the parent, so the upper bound becomes smaller
            # When you go right, the node’s value must be greater than the parent, so the lower bound becomes larger
            if not (left < node.val < right):
                return False
            # Every node carries the full allowed range, not only the parent, that's how we check violations
            # that can happen if somewhere below in the right a value is lower than in the left
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        return valid(root, float("-inf"), float("inf"))