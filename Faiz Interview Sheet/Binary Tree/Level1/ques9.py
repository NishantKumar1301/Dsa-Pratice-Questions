#Question : Binary Tree Maximum Path Sum
#Link to the question: https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxPath(self,root,maxi):
        if not root:
            return 0
        left = max(0,self.maxPath(root.left,maxi))
        right = max(0,self.maxPath(root.right,maxi))
        maxi[0]=max(maxi[0],root.val+left+right)
        return root.val+max(left,right)

    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        maxi = [float('-inf')]
        self.maxPath(root,maxi)
        return maxi[0]
        