#Question : Maximum Depth of Binary Tree
#Link to the question:  https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        queue=deque([root])
        ans = 0
        if not root:
            return 0
        while queue:
            length  = len(queue)
            for _ in range(length):
                curr= queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            ans+=1
        return ans
