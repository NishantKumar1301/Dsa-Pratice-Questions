#Question : Binary Tree Right Side View
#Link to the question: https://leetcode.com/problems/binary-tree-right-side-view/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverse_preorder(self,node,level,ans):#Actual preorder = root,left , right REVERSED = root,right, left
        if not node:
            return 
        if level==len(ans):
            ans.append(node.val)
        self.reverse_preorder(node.right,level+1,ans)
        self.reverse_preorder(node.left,level+1,ans)
 
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ans = []
        if not root:
            return []
        self.reverse_preorder(root,0,ans)
        return ans
        
        