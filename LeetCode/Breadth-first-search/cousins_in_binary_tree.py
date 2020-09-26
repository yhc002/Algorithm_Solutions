"""
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

Constraints:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
"""

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        current = [root]
        while len(current)>0:
            next_depth=[]
            found_x = False
            found_y = False
            for n in current:
                if n.left and n.right:  
                    if (n.left.val==x and n.right.val==y) or (n.left.val==y and n.right.val==x):
                        return False
                if n.left:
                    if n.left.val == x:
                        found_x = True
                    if n.left.val ==y:
                        found_y = True
                    next_depth.append(n.left)
                if n.right:
                    if n.right.val == x:
                        found_x = True
                    if n.right.val ==y:
                        found_y = True
                    next_depth.append(n.right)
                if found_x and found_y:
                    return True
            current = next_depth
            if found_x:
                return False
            if found_y:
                return False
        return False
