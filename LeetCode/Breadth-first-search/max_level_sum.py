"""
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes at level X is maximal.


Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        stack=[root]
        maxSum=root.val
        maxLevel=1
        level=1
        while len(stack)>0:
            levelSum=0
            newStack=[]
            for node in stack:
                levelSum+=node.val
                if node.left:
                    newStack.append(node.left)
                if node.right:
                    newStack.append(node.right)
            if maxSum<levelSum:
                maxSum=levelSum
                maxLevel=level
            stack=newStack
            level+=1
        return maxLevel
