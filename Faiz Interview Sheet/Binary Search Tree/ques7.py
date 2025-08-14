#Question : Construct Binary Search Tree from Preorder Traversal
#Link to the question: https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def build_bst_tree(self,preorder,prestart,preend,inorder,instart,inend,inmap):
        if prestart>preend or instart>inend:
            return None
        root = TreeNode(preorder[prestart])
        inroot = inmap[root.val]
        numleft = inroot - instart
        root.left = self.build_bst_tree(preorder,prestart+1,prestart+numleft,inorder,instart,inroot-1,inmap)
        root.right = self.build_bst_tree(preorder,prestart+numleft+1,preend,inorder,inroot+1,inend,inmap)
        return root
        
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: Optional[TreeNode]
        """
        #Inorder traversal in bst  returns the list in the sorted manner
        inorder = sorted(preorder)
        n = len(preorder)
        #in preorder root is always the first , root-> left-> right
        inmap = {}
        for i in range(n):
            inmap[inorder[i]]=i
        root = self.build_bst_tree(preorder,0,n-1,inorder,0,n-1,inmap)
        return root
        