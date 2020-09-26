"""
Given a binary tree, return the sum of values of its deepest leaves.

Constraints:

The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        stack = [root]
        while len(stack)>0:
            new_stack = []
            total = 0
            for n in stack:
                total+=n.val
                if n.left:
                    new_stack.append(n.left)
                if n.right:
                    new_stack.append(n.right)
            if len(new_stack)==0:
                return total
            stack = new_stack
