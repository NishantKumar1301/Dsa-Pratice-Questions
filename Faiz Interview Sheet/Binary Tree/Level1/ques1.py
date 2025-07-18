#Question : Binary Tree Preorder Traversal
#Link to the question:  https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root is None:
            return []
        ans = [root.val]
        ans += self.preorderTraversal(root.left)
        ans+=self.preorderTraversal(root.right)
        return ans
