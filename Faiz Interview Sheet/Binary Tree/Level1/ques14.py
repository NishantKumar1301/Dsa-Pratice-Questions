#Question : Lowest Common Ancestor of a Binary Tree
#Link to the question: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root==p or root==q:
            return root
        leftside = self.lowestCommonAncestor(root.left,p,q)
        rightside = self.lowestCommonAncestor(root.right,p,q)
        if not leftside:
            return rightside
        elif not rightside:
            return leftside
        else:
            return root
        