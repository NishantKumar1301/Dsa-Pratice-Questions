#Question : Validate Binary Search Tree
#Link to the question: https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def helper(self,root,mini, maxi):
        if root is None:
            return True
        if root.val<mini  or root.val>maxi:
            return False
        return self.helper(root.left,mini,root.val) and self.helper(root.right,root.val,maxi)
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.helper(root,float('-inf'), float('inf'))
        