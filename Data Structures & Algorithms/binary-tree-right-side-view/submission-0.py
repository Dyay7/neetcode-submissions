# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, depth):
            if not node:
                return None
            if depth == len(res):
                res.append(node.val) # if we still didn't add anything for this level we add node.val
            dfs(node.right, depth + 1) # this way if there's a right node it will be added
            dfs(node.left, depth + 1) # when there are no more right nodes left this 
            # will make sure to add the needed left ones in the levels left

        dfs(root, 0)
        return res