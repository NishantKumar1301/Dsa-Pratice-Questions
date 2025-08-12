#Question : Delete Node in a BST
#Link to the question: https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        if root.val == key:
            return self.helper(root)
        dummy = root
        while root is not None:
            if key>root.val:
                #traverse through the right subtree
                if root.right is not None and root.right.val ==key:
                    root.right = self.helper(root.right)
                    break
                else:
                    root = root.right
            else:
                #Traverse through the left part
                if root.left is not None and root.left.val==key:
                    root.left = self.helper(root.left)
                    break
                else:
                    root = root.left
        return dummy
    
    def helper(self,root):
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        rightNode = root.right
        lastRightNode = self.find_last_right_node_of_left_tree(root.left)
        lastRightNode.right = rightNode
        return root.left
    
    def find_last_right_node_of_left_tree(self,root):
        if root.right is None:
            return root
        return self.find_last_right_node_of_left_tree(root.right)