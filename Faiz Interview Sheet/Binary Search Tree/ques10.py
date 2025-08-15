#Question : Recover Binary Search Tree
#Link to the question: https://leetcode.com/problems/recover-binary-search-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorder_traversal(self,root,inorder):
        if not root:
            return 
        self.inorder_traversal(root.left,inorder)
        inorder.append(root)
        self.inorder_traversal(root.right,inorder)

    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        inorder = []
        self.inorder_traversal(root,inorder)
        first=middle=last = None
        for i in range(len(inorder)-1):
            if inorder[i].val>inorder[i+1].val:
                if not first:
                    first,middle = inorder[i],inorder[i+1]
                else:
                    last = inorder[i+1]
        #Case 1 : The swpping elements are not adjacent to each other
        if last is not None:
            first.val,last.val = last.val,first.val
        else:
            #Case 2 : The swapped elements are adjacent to each other
            first.val,middle.val = middle.val,first.val
        