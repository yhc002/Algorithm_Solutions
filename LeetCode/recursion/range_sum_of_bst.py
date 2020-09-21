# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def checkNode(n):
            if not n:
                return 0
            if n.val<L:
                return checkNode(n.right)
            if n.val>R:
                return checkNode(n.left)
            return n.val + checkNode(n.left) + checkNode(n.right)
        
        return checkNode(root)
        
