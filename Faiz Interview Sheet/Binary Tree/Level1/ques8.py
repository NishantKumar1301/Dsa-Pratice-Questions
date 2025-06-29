#Question : Diameter of Binary Tree
#Link to the question:  https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMaxHeight(self,root,diameter):
        if not root:
            return 0
        left_height = self.findMaxHeight(root.left,diameter)
        right_height = self.findMaxHeight(root.right,diameter)
        diameter[0] = max(diameter[0],left_height+right_height)
        return 1+max(left_height,right_height)

    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        diameter = [0]
        self.findMaxHeight(root,diameter)
        return diameter[0]
        