#Question : Reverse Odd Levels of Binary Tree
#Link to the question: https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/?envType=daily-question&envId=2024-12-20

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        queue = deque([root])
        level =0 
        while queue:
            length = len(queue)
            level_node =[]
            for i in range(length):
                curr_node = queue.popleft()
                level_node.append(curr_node)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            
            if level%2==1:
                for j in range(len(level_node)//2):
                    level_node[j].val,level_node[len(level_node)-j-1].val= level_node[len(level_node)-j-1].val,level_node[j].val
            level+=1
        
        return root


