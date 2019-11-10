# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def checkNode(l,r):
            if l==None and r==None:
                return True
            if l!=None and r!=None and l.val==r.val:
                return checkNode(l.left,r.left) and checkNode(l.right,r.right)
            return False
        return checkNode(p,q)
