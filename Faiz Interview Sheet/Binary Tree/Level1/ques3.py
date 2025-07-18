#Question : Binary Tree Postorder Traversal
#Link to the question:  https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root is None:
            return []
        ans = []
        ans+=self.postorderTraversal(root.left)
        ans+=self.postorderTraversal(root.right)
        ans+=[root.val]
        return ans