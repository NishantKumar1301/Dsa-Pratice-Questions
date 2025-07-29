#Question : All Nodes Distance K in Binary Tree
#Link to the question:https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque , defaultdict

class Solution(object):
    def mark_parent(self,root,parent_track):
        queue = deque([root])
        while queue:
            curr = queue.popleft()
            if curr.left:
                parent_track[curr.left]=curr
                queue.append(curr.left)
            if curr.right:
                parent_track[curr.right]=curr
                queue.append(curr.right)

    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        if not root:
            return []
        visited = defaultdict(bool)
        queue = deque([target])
        visited[target] = True
        curr_level = 0
        parent_track={}
        self.mark_parent(root,parent_track)
        while queue:
            if curr_level==k:
                break
            length = len(queue)
            for _ in range(length):
                curr = queue.popleft()
                for ngbr in (curr.left,curr.right,parent_track.get(curr)):
                    if ngbr and not visited[ngbr]:
                        visited[ngbr]=True
                        queue.append(ngbr)
            curr_level+=1
        return [node.val for node in queue ]
        