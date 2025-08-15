#Question : Two Sum IV - Input is a BST
#Link to the question: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def generate_inorder(self,root,inorder):
        if not root:
            return 
        self.generate_inorder(root.left,inorder)
        inorder.append(root.val)
        self.generate_inorder(root.right,inorder)

    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        inorder = []
        self.generate_inorder(root,inorder)
        n = len(inorder)
        left,right = 0,n-1
        while left<right:
            sum_ =  inorder[left]+inorder[right]
            if sum_==k:
                return True
            elif sum_ >k:
                right-=1
            else:
                left+=1
        return False