#Question : Construct Binary Tree from Inorder and Postorder Traversal
#Link to the question: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        inmap = {}
        for i in range(len(inorder)):
            inmap[inorder[i]]=i
        return self.builder(inorder,0,len(inorder)-1,postorder,0,len(postorder)-1,inmap)
    
    def builder(self,inorder,instart,inend,postorder,poststart,postend,inmap):
        if instart>inend or poststart>postend:
            return None
        root = TreeNode(postorder[postend])
        inroot = inmap[root.val]
        numleft = inroot-instart
        root.left = self.builder(inorder,instart,inroot-1,postorder,poststart,poststart+numleft-1,inmap)
        root.right = self.builder(inorder,inroot+1,inend,postorder,poststart+numleft,postend-1,inmap)
        return root
        