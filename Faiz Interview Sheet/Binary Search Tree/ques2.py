#Question : Insert into a Binary Search Tree
#Link to the question: https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        #If the tree is empty then create a node and return it
        if root is None:
            return TreeNode(val)
        curr = root
        while True:
            #If val > curr.val: append it in the right subtree
            if val > curr.val:
                if curr.right is not None:
                    curr = curr.right
                else:
                    curr.right = TreeNode(val)
                    break
            else:
                #Append it in the left subtree
                if curr.left is not None:
                    curr = curr.left
                else:
                    curr.left = TreeNode(val)
                    break
        return root