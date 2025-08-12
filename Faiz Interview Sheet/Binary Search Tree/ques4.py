#Question : Kth Smallest Element in a BST
#Link to the question: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self,root,arr):
        if not root:
            return None
        self.inorderTraversal(root.left,arr)
        arr.append(root.val)
        self.inorderTraversal(root.right,arr)
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        #Note : In bst inorder traversal gives the sorted version of the tree
        arr = []
        self.inorderTraversal(root,arr) #arr will now contain all the elements in the sorted manner
        return arr[k-1]
