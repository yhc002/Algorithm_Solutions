"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Constraints:
  The number of nodes in the binary tree is in the range [1, 10^5].
  Each node's value is between [-10^4, 10^4].
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def check(node,val):
            if not node:
                return 0
            if node.val>=val:
                return 1 + check(node.left,node.val) + check(node.right,node.val)
            return check(node.left,val) + check(node.right,val)
        return check(root,root.val)
