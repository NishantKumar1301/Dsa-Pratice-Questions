#Question : Maximum Width of Binary Tree
#Link to the question:https://leetcode.com/problems/maximum-width-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        ans =0
        queue = deque([(root,0)])
        if not root:
            return 0
        while queue:
            length = len(queue)
            first_pos = queue[0][1]
            first , last = None,None
            for i in range(length):
                node,pos = queue.popleft()
                curr_pos = pos-first_pos
                if i==0:
                    first = curr_pos
                if i==length-1:
                    last = curr_pos
                if node.left:
                    queue.append((node.left,2*curr_pos+1))
                if node.right:
                    queue.append((node.right,2*curr_pos+2))
            ans = max(ans,last-first+1)
        return ans
