#Question : Lowest Common Ancestor of a Binary Search Tree
#Link to the question: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None or root==p  or root==q:
            return root
        leftSide  = self.lowestCommonAncestor(root.left,p,q)
        rightSide = self.lowestCommonAncestor(root.right,p,q)
        if leftSide is None:
            return rightSide
        elif rightSide is None:
            return leftSide
        else:
            return root