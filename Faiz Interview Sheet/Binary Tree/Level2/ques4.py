#Question : Construct Binary Tree from Preorder and Inorder Traversal
#Link to the question: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        inmap ={}
        for i in range(len(inorder)):
            inmap[inorder[i]]=i
        root= self.builder(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1,inmap)
        return root
    
    def builder(self,preorder,prestart,preend,inorder,instart,inend,inmap):
        if prestart>preend or instart>inend:
            return None
        root=TreeNode(preorder[prestart])
        inroot = inmap[root.val] #Position of root in the inorder map
        numleft = inroot-instart
        root.left = self.builder(preorder,prestart+1,prestart+numleft,inorder,instart,inroot-1,inmap)
        root.right = self.builder(preorder,prestart+numleft+1,preend,inorder,inroot+1,inend,inmap)
        return root
        