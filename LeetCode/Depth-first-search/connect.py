"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root==None:
            return root
        def linkNext(node,rightSib):
            if node.left==None:
                return
            node.left.next=node.right
            linkNext(node.left,node.right)
            
            if rightSib!=None:
                node.right.next=rightSib.left
                linkNext(node.right,rightSib.left)
            else:
                node.right.next=None
                linkNext(node.right,None)
            
        linkNext(root,None)
        
        return root
