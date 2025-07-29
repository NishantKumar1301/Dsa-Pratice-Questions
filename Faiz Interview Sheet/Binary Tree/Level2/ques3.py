#Question : Count Complete Tree Nodes
#Link to the question: https://leetcode.com/problems/count-complete-tree-nodes/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        # Method 1 : Time complexity = O(n)
        # if not root:
        #     return 0
        # ans = 0
        # queue = deque([root])
        # while queue:
        #     curr= queue.popleft()
        #     ans+=1
        #     if curr.left:
        #         queue.append(curr.left)
        #     if curr.right:
        #         queue.append(curr.right)
        # return ans
        
        #Method 2 : 

        #Calculate left and right height if both are equal then return 2**h-1 else 1+recursive(left)+recurive(right)
        if not root:
            return 0
        left_height = self.find_left_height(root)
        right_height = self.find_right_height(root)
        if left_height==right_height:
            # return 2**left_height-1 , power of x = 1<<x
            return (1<<left_height)-1
        else:
            return 1+self.countNodes(root.left)+self.countNodes(root.right)
    
    def find_left_height(self,root):
        height= 0
        while root:
            height+=1
            root= root.left
        return height
    
    def find_right_height(self,root):
        height = 0
        while root:
            height+=1
            root = root.right
        return height