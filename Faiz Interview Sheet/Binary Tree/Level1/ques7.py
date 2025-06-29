#Question : Balanced Binary Tree
#Link to the question:  https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def find_height(self,root):
        if not root:
            return 0
        left_height = self.find_height(root.left)
        right_height = self.find_height(root.right)
        #If any node dont follow the condition return -1
        if left_height==-1 or right_height==-1:
            return -1
        if abs(left_height-right_height)>1:
            return -1
        #Height = max( left, right)+1
        return max(left_height,right_height)+1

    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        #If find_height funtion != -1 then it is balanced
        return self.find_height(root)!=-1
        
        