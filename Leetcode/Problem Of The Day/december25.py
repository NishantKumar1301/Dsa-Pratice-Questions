#Question : Find Largest Value in Each Tree Row
#Link to the question: https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/?envType=daily-question&envId=2024-12-25


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def find_maximum(self,arr):
        return max(arr)
    
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        queue =deque([root])
        ans =[]
        while queue:
            arr =[]*len(queue)
            for _ in range(len(queue)):
                curr = queue.popleft()
                arr.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            ans.append(self.find_maximum(arr))
        return ans
        