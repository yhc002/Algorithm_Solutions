"""
Given a binary tree, find the leftmost value in the last row of the tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        stack=[root]
        lastL=root.val
        while len(stack)>0:
            newStack=[]
            lastL=stack[0].val
            for node in stack:
                if node.left:
                    newStack.append(node.left)
                if node.right:
                    newStack.append(node.right)
            stack=newStack
        return lastL
