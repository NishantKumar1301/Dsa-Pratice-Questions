#Question : Symmetric Tree
#Link to the question: https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution(object):
#     def helper(self,leftside,rightside):
#         if not leftside or not rightside:
#             if leftside==rightside:
#                 return True
#             else:
#                 return False
        
#         if leftside.val!=rightside.val:
#             return False
#         return self.helper(leftside.left,rightside.right) and self.helper(leftside.right,rightside.left)
#     def isSymmetric(self, root):
#         """
#         :type root: Optional[TreeNode]
#         :rtype: bool
#         """
#         if not root:
#             return True
#         return self.helper(root.left,root.right)

class Solution(object):
    def helper(self,leftside,rightside):
        if not leftside or not rightside:
            return leftside==rightside
        if leftside.val!=rightside.val:
            return False
        return self.helper(leftside.left,rightside.right) and self.helper(leftside.right,rightside.left)
        
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        return self.helper(root.left,root.right)