#Question : Same tree
#Link to the question:  https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        #Do preorder traversal if both the traversal gives same result then true else false
        if p is None and q is None:
            return True
        if (p is None and q is not None) or (p is not None and q is None):
            return False
        if (p.val==q.val and self.isSameTree(p.left,q.left) and (self.isSameTree(p.right,q.right))):
            return True
        else:
            return False